import requests
from innexiaBot import dispatcher
from innexiaBot.modules.disable import DisableAbleCommandHandler
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async


@run_async
def paste(update, context):
    args = context.args
    BURL = "https://del.dog"
    message = update.effective_message
    if message.reply_to_message:
        data = message.reply_to_message.text
    elif len(args) >= 1:
        data = message.text.split(None, 1)[1]
    else:
        message.reply_text("What am I supposed to do with this?!")
        return

    r = requests.post(f"{BURL}/documents", data=data.encode("utf-8"))

    if r.status_code == 404:
        update.effective_message.reply_text("Failed to reach dogbin")
        r.raise_for_status()

    res = r.json()

    if r.status_code != 200:
        update.effective_message.reply_text(res["message"])
        r.raise_for_status()

    key = res["key"]
    if res["isUrl"]:
        reply = "Shortened URL: {}/{}\nYou can view stats, etc. [here]({}/v/{})".format(
            BURL, key, BURL, key
        )
    else:
        reply = f"{BURL}/{key}"
    update.effective_message.reply_text(
        reply, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True
    )


PASTE_HANDLER = DisableAbleCommandHandler("paste", paste)
dispatcher.add_handler(PASTE_HANDLER)

__command_list__ = ["paste"]
__handlers__ = [PASTE_HANDLER]

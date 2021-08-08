import requests
from innexiaBot import dispatcher
from innexiaBot.modules.disable import DisableAbleCommandHandler
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async


@run_async
def paste(update, context):
    args = context.args
    BURL = "https://hastebin.com"
    message = update.effective_message.encode("utf-8")
    if message.reply_to_message:
        data = message.reply_to_message.text.encode("utf-8")
    elif len(args) >= 1:
        data = message.text.split(None, 1)[1].encode("utf-8")
    else:
        message.reply_text("What am I supposed to do with this?!")
        return

    r = requests.post(f"{BURL}/documents", data=data)

    if r.status_code == 404:
        update.effective_message.reply_text("Failed to reach nekoBin")
        r.raise_for_status()

    res = r.json()
    key = res["key"]
    update.effective_message.reply_text(f"Pasted To [HasteBin](https://HasteBin.com/{key})!")



PASTE_HANDLER = DisableAbleCommandHandler("paste", paste)
dispatcher.add_handler(PASTE_HANDLER)

__command_list__ = ["paste"]
__handlers__ = [PASTE_HANDLER]

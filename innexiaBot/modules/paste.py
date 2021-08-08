import requests
from innexiaBot import dispatcher
from innexiaBot.modules.disable import DisableAbleCommandHandler
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async


@run_async
 async def paste_(message: Message) -> None:
    """pastes the text directly to dogbin or nekobin"""
    await message.edit("`Processing...`")
    text = message.filtered_input_str
    replied = message.reply_to_message
    use_neko = False
    file_ext = ".txt"
    if not text and replied:
        if replied.document and replied.document.file_size < 2 ** 20 * 10:
            file_ext = os.path.splitext(replied.document.file_name)[1]
            path = await replied.download(Config.DOWN_PATH)
            with open(path, "r") as d_f:
                text = d_f.read()
            os.remove(path)
        elif replied.text:
            text = replied.text
    if not text:
        await message.err("input not found!")
        return
    flags = list(message.flags)
    if "n" in flags:
        use_neko = True
        flags.remove("n")
    if flags and len(flags) == 1:
        file_ext = "." + flags[0]
    await message.edit("`Pasting text ...`")
    async with aiohttp.ClientSession() as ses:
        if use_neko:
            async with ses.post(
                NEKOBIN_URL + "api/documents", json={"content": text}
            ) as resp:
                if resp.status == 201:
                    response = await resp.json()
                    key = response["result"]["key"]
                    final_url = NEKOBIN_URL + key + file_ext
                    reply_text = f"**Nekobin** [URL]({final_url})"
                    await message.edit(reply_text, disable_web_page_preview=True)
                else:
                    await message.err("Failed to reach Nekobin")
        else:
            async with ses.post(
                DOGBIN_URL + "documents", data=text.encode("utf-8")
            ) as resp:
                if resp.status == 200:
                    response = await resp.json()
                    key = response["key"]
                    final_url = DOGBIN_URL + key
                    if response["isUrl"]:
                        reply_text = (
                            f"**Shortened** [URL]({final_url})\n"
                            f"**Dogbin** [URL]({DOGBIN_URL}v/{key})"
                        )
                    else:
                        reply_text = f"**Dogbin** [URL]({final_url}{file_ext})"
                    await message.edit(reply_text, disable_web_page_preview=True)
                else:
                    await message.err("Failed to reach Dogbin")
    
        reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True
    )


PASTE_HANDLER = DisableAbleCommandHandler("paste", paste)
dispatcher.add_handler(PASTE_HANDLER)

__command_list__ = ["paste"]
__handlers__ = [PASTE_HANDLER]

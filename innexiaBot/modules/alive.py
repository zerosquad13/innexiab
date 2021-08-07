# COPYRIGHT (C) 2021 @Autichrist AND @useless

from telethon import events, Button, custom
import re, os
from InnexiaBot.events import register
from innexiaBot import telethn as tbot
from innexiaBot import telethn as tgbot
from innexiaBot import (SUPPORT_CHAT, OWNER_USERNAME)

PHOTO = "https://telegra.ph/file/c78acfb14cedec2d23c48.jpg"
@register(pattern=("/alive"))
async def awake(event):
  koraXname = event.sender.first_name
  koraX = f"Hello {koraXname}, I am innexia\n\n"
  koraX += "🔸 I'm Working Properly\n\n"
  koraX += "🔹 Innexia OS : 2.0 LATEST\n\n"
  koraX += f"🔸 My Master {OWNER_USERNAME} ☺️\n\n"
  koraX += "🔹 I'm Updated\n\n"
  koraX += "🔸 Telethon : 1.19.5 latest\n\n"
  koraX += "thank You for Add me Here"
  BUTTON = [[Button.url("SUPPORT", f"https://t.me/{SUPPORT_CHAT}"), Button.url("DEVLOPER", f"https://t.me/{OWNER_USERNAME}")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=koraX,  buttons=BUTTON)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"KoraX")))
async def callback_query_handler(event):
# inline by kittu5588 🔥
  kittu = [[Button.url("REPO", "https://github.com/MrSammyXD"), Button.url("REPO-USERBOT", "https://github.com/kora-network/korauserbot")]]
  kittu +=[[Button.url("SUPPORT CHANNEL", "https://t.me/korateam"), Button.url("SUPPORT GROUP", "https://t.me/SUPPORT_CHAT")]]
  kittu +=[[custom.Button.inline("ALIVE", data="kittu")]]
  await event.edit(text=f"ALL DETAILS OF REPOS", buttons=kittu)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"kittu")))
async def callback_query_handler(event):
  global PHOTO
  koraXname = event.sender.first_name
  koraX = f" Hello {koraXname}, I'm innexia\n\n"
  koraX += "🔸 I'm Working Properly\n\n"
  koraX += "🔹 Innexia OS : 2.0 LATEST\n\n"
  koraX += f"🔸 My Master {OWNER_USERNAME} ☺️\n\n"
  koraX += "🔹 I'm Updated\n\n"
  koraX += "🔸 Telethon : 1.19.5 latest\n\n"
  koraX += "thank You for Add me Here"
  BUTTON = [[Button.url("SUPPORT", f"https://t.me/{SUPPORT_CHAT}"), Button.url("DEVLOPER", f"https://t.me/{OWNER_USERNAME}")]]
  await event.edit(text=koraX, buttons=BUTTONS)


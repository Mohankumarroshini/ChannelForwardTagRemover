import os, asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait

bot = Client(
    "Remove FwdTag",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


START_TXT = """
ʜɪ {}, ɪ'ᴍ ғᴏʀᴡᴀʀᴅ ᴛᴀɢ ʀᴇᴍᴏᴠᴇʀ ʙᴏᴛ [🤖](https://telegra.ph/file/57873ee2279555866f4c9.jpg) .\n\nғᴏʀᴡᴀʀᴅ ᴍᴇ sᴏᴍᴇ ᴍᴇssᴀɢᴇs, ɪ ᴡɪʟʟ ʀᴇᴍᴏᴠᴇ ғᴏʀᴡᴀʀᴅ ᴛᴀɢ ғʀᴏᴍ ᴛʜᴇᴍ.\nᴀʟsᴏ ᴄᴀɴ ᴅᴏ ɪᴛ ɪɴ ᴄʜᴀɴɴᴇʟs.
"""

START_BTN = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ᴜᴘᴅᴀᴛᴇs', url='https://t.me/tamilbots'),
        ]]
    )


@bot.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TXT.format(update.from_user.mention)
    reply_markup = START_BTN
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@bot.on_message(filters.channel & filters.forwarded)
async def fwdrmv(c, m):
    try:
        if m.media and not (m.video_note or m.sticker):
            await m.copy(m.chat.id, caption = m.caption if m.caption else None)
            await m.delete()
        else:
            await m.copy(m.chat.id)
            await m.delete()
    except FloodWait as e:
        await asyncio.sleep(e.x)


@bot.on_message(filters.private | filters.group)
async def fwdrm(c, m):
    try:
        if m.media and not (m.video_note or m.sticker):
            await m.copy(m.chat.id, caption = m.caption if m.caption else None)
        else:
            await m.copy(m.chat.id)
    except FloodWait as e:
        await asyncio.sleep(e.x)


bot.run()

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("https://telegra.ph/file/26d1fa8e4642ab680305a.jpg")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

𝐇𝐢𝐢, 𝐈 𝐦 𝐇𝐞𝐫𝐞 𝐇𝐞𝐥𝐩 𝐔 𝐌𝐚𝐧𝐚𝐠𝐞 𝐔𝐫 𝐕𝐂 𝐄𝐚𝐬𝐢𝐥𝐲.
𝐖𝐢𝐭𝐡 𝐋𝐨𝐭𝐬 𝐎𝐟 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐢𝐧 𝐭𝐡𝐢𝐬 𝐛𝐨𝐭
𝐕𝐄𝐗𝐀𝐍𝐀 𝐈𝐬 𝐚𝐧 𝐀𝐝𝐯𝐚𝐧𝐜𝐞𝐝 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 𝐛𝐨𝐭.

𝐦𝐲 𝐎𝐰𝐧𝐞𝐫 𝐈𝐬 :- @op_badnam


𝐂𝐫𝐞𝐝𝐢𝐭𝐬:- @vexana_support

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Owner 🛠", url="https://t.me/Op_Badnam")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/vexana_Support"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/vexana_updates"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/badnam_ro_bot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Badman Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/vexana_support")
                ]
            ]
        )
   )



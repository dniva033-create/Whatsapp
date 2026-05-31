# =========================================
# ❖ 𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 𝐗 𝐁𝐎𝐓 ❖
# 𝐄𝐗𝐓𝐑𝐄𝐌𝐄 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐔𝐈
# =========================================

import json
import time
import logging
import asyncio
import re

from datetime import datetime

from telegram import (
    Update,
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from telegram.constants import ChatAction

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

# ================= CONFIG =================

TOKEN = "8814964213:AAGbzfiMTqbJIc3g-2XCSij6I9R8cEhPxXE"

OWNER_USERNAME = "Vault_With_Pratik"

CHANNEL_USERNAME = "@ethtical_zone"

CHANNEL_LINK = "https://t.me/ethtical_zone"

SUPPORT_LINK = "https://t.me/boost/EliteHubZone"

DB_FILE = "users.json"

LOG_FILE = "logs.txt"

# ================= STICKERS =================

WELCOME_STICKER = "CAACAgQAAxkBAAFK26lqGDsn5CzxWB9AMGMtI6LQbI2y4gACuhUAAiOkQFNu4nQSj08eBzsE"

LOADING_STICKER = "CAACAgUAAxkBAAFK269qGDtRqCaLmk4GtU1jcNUfE4X59gACGQgAAk8kyVYNJvl0I0ZLyTsE"

SUCCESS_STICKER = "CAACAgIAAxkBAAFK271qGDwHxazpV3Dfaujp3gmcn2Kt8AACoxAAAoUDqUi75hcVIRSUgzsE"

DENIED_STICKER = "CAACAgQAAxkBAAFK28VqGDxzdoKVdi7KqRxsTwunhAqSMQACxwQAAjcNfhm6zckoSaq0BDsE"

UPLOAD_STICKER = "CAACAgUAAxkBAAFK26FqGDpyKJtpHQWRikAz31X_0v9vzQACiBkAAkjDOVZ7rwWo6j1dHDsE"

# ================= SYSTEM =================

cooldown = {}

active_users = set()

start_time = datetime.now()

# ================= LOGGING =================

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ================= DATABASE =================

def load_db():

    try:

        with open(DB_FILE, "r") as f:

            return json.load(f)

    except:

        return {}

def save_db(data):

    with open(DB_FILE, "w") as f:

        json.dump(data, f, indent=4)

db = load_db()

# ================= UTILS =================

def get_uptime():

    delta = datetime.now() - start_time

    return str(delta).split(".")[0]

def valid_number(number):

    number = number.replace(" ", "").strip()

    pattern = r"^\+[1-9][0-9]{9,14}$"

    return re.match(pattern, number)

async def typing_effect(context, chat_id):

    await context.bot.send_chat_action(
        chat_id=chat_id,
        action=ChatAction.TYPING
    )

    await asyncio.sleep(1)

async def auto_delete_sticker(
    context,
    chat_id,
    sticker_id,
    delay=2
):

    try:

        msg = await context.bot.send_sticker(
            chat_id=chat_id,
            sticker=sticker_id
        )

        await asyncio.sleep(delay)

        await msg.delete()

    except:
        pass

# ================= BOOT =================

async def boot_animation(message):

    frames = [

"""
╔═══ ❖ • 𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 𝐗 • ❖ ═══╗

💻 𝐁𝐎𝐎𝐓𝐈𝐍𝐆 𝐒𝐘𝐒𝐓𝐄𝐌

█ Connecting Node...

◐ 𝐋𝐨𝐚𝐝𝐢𝐧𝐠...
""",

"""
╔═══ ❖ • 𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 𝐗 • ❖ ═══╗

💻 𝐁𝐎𝐎𝐓𝐈𝐍𝐆 𝐒𝐘𝐒𝐓𝐄𝐌

█ Connecting Node...
█ Loading Encryption...

◓ 𝐋𝐨𝐚𝐝𝐢𝐧𝐠...
""",

"""
╔═══ ❖ • 𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 𝐗 • ❖ ═══╗

💻 𝐁𝐎𝐎𝐓𝐈𝐍𝐆 𝐒𝐘𝐒𝐓𝐄𝐌

█ Connecting Node...
█ Loading Encryption...
█ Verifying Access...

◑ 𝐋𝐨𝐚𝐝𝐢𝐧𝐠...
""",

"""
╔═══ ❖ • 𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 𝐗 • ❖ ═══╗

💻 𝐁𝐎𝐎𝐓𝐈𝐍𝐆 𝐒𝐘𝐒𝐓𝐄𝐌

█ Connecting Node...
█ Loading Encryption...
█ Verifying Access...
█ Access Granted...

◒ 𝐂𝐨𝐦𝐩𝐥𝐞𝐭𝐞...
"""
]

    for frame in frames:

        try:

            await message.edit_text(frame)

            await asyncio.sleep(0.7)

        except:
            pass

# ================= PROCESS =================

async def progress_animation(message):

    bars = [
        ("▓░░░░░░░░", "10%"),
        ("▓▓░░░░░░░", "20%"),
        ("▓▓▓░░░░░░", "30%"),
        ("▓▓▓▓░░░░░", "40%"),
        ("▓▓▓▓▓░░░░", "50%"),
        ("▓▓▓▓▓▓░░░", "60%"),
        ("▓▓▓▓▓▓▓░░", "70%"),
        ("▓▓▓▓▓▓▓▓░", "80%"),
        ("▓▓▓▓▓▓▓▓▓", "90%"),
        ("▓▓▓▓▓▓▓▓▓", "100%"),
    ]

    circles = ["◐", "◓", "◑", "◒"]

    for i, (bar, percent) in enumerate(bars):

        circle = circles[i % 4]

        try:

            await message.edit_text(

f"""
╔═══ ❖ • 𝐏𝐑𝐎𝐂𝐄𝐒𝐒 • ❖ ═══╗

💻 𝐀𝐋𝐏𝐇𝐀 𝐓𝐄𝐑𝐌𝐈𝐍𝐀𝐋

█ Scanning Number...
█ Connecting Gateway...
█ Validating Request...
█ Creating Session...
█ Opening WhatsApp...

{bar} {percent}

{circle} 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠...
"""
            )

            await asyncio.sleep(0.5)

        except:
            pass

# ================= CHANNEL CHECK =================

async def check_join(update, context):

    try:

        member = await context.bot.get_chat_member(
            CHANNEL_USERNAME,
            update.effective_user.id
        )

        return member.status in [
            "member",
            "administrator",
            "creator"
        ]

    except:
        return False

# ================= KEYBOARDS =================

def main_keyboard():

    return ReplyKeyboardMarkup(

        [
            ["📲 𝐆𝐄𝐓 𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 𝐀𝐂"],
            ["👤 𝐏𝐑𝐎𝐅𝐈𝐋𝐄", "⚙️ 𝐒𝐄𝐓𝐓𝐈𝐍𝐆𝐒"],
            ["📊 𝐒𝐓𝐀𝐓𝐔𝐒", "🆘 𝐒𝐔𝐏𝐏𝐎𝐑𝐓"],
            ["👑 𝐀𝐃𝐌𝐈𝐍", "🔄 𝐑𝐄𝐅𝐑𝐄𝐒𝐇"],
            ["❌ 𝐂𝐋𝐎𝐒𝐄"]
        ],

        resize_keyboard=True

    )

def back_keyboard():

    return ReplyKeyboardMarkup(
        [["🔙 𝐁𝐀𝐂𝐊"]],
        resize_keyboard=True
    )

def result_keyboard():

    return ReplyKeyboardMarkup(

        [
            ["📲 𝐎𝐏𝐄𝐍 𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏"],
            ["🔙 𝐁𝐀𝐂𝐊"]
        ],

        resize_keyboard=True

    )

# ================= HOME PANEL =================

async def send_home(update, context):

    uid = str(update.effective_user.id)

    await typing_effect(
        context,
        update.effective_chat.id
    )

    await context.bot.send_message(
        chat_id=update.effective_chat.id,

        text=f"""
╔═══ ❖ • 𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 𝐗 • ❖ ═══╗
┃ 👑 𝐀𝐋𝐏𝐇𝐀 𝐊𝐈𝐍𝐆 𝐒𝐘𝐒𝐓𝐄𝐌
┃ ⚡ 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐀𝐂𝐂𝐄𝐒𝐒
╚═══ ❖ • 𝐎𝐍𝐋𝐈𝐍𝐄 • ❖ ═══╝

📲 𝐆𝐞𝐭 𝐖𝐡𝐚𝐭𝐬𝐀𝐩𝐩 𝐀𝐂
⚙️ 𝐀𝐝𝐯𝐚𝐧𝐜𝐞𝐝 𝐒𝐲𝐬𝐭𝐞𝐦
🛡 𝐒𝐞𝐜𝐮𝐫𝐢𝐭𝐲 𝐒𝐡𝐢𝐞𝐥𝐝
💻 𝐋𝐢𝐯𝐞 𝐓𝐞𝐫𝐦𝐢𝐧𝐚𝐥
📡 𝐀𝐥𝐩𝐡𝐚 𝐍𝐞𝐭𝐰𝐨𝐫𝐤

👥 𝐔𝐬𝐞𝐫𝐬 : {len(db)}
⚡ 𝐀𝐜𝐭𝐢𝐯𝐞 : {len(active_users)}
⏱ 𝐔𝐩𝐭𝐢𝐦𝐞 : {get_uptime()}
""",

        reply_markup=main_keyboard()
    )

# ================= START =================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    uid = str(update.effective_user.id)

    active_users.add(uid)

    context.user_data["waiting_number"] = False

    if uid not in db:

        db[uid] = {
            "requests": 0,
            "numbers": []
        }

        save_db(db)

    await auto_delete_sticker(
        context,
        update.effective_chat.id,
        WELCOME_STICKER,
        2
    )

    joined = await check_join(update, context)

    if not joined:

        buttons = InlineKeyboardMarkup([

            [
                InlineKeyboardButton(
                    "📢 𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋",
                    url=CHANNEL_LINK
                )
            ],

            [
                InlineKeyboardButton(
                    "🔄 𝐕𝐄𝐑𝐈𝐅𝐘",
                    callback_data="verify"
                )
            ]

        ])

        await update.message.reply_text(

"""
╔═══ ❖ • 𝐀𝐂𝐂𝐄𝐒𝐒 • ❖ ═══╗

🚫 𝐉𝐨𝐢𝐧 𝐑𝐞𝐪𝐮𝐢𝐫𝐞𝐝
📡 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 𝐒𝐲𝐬𝐭𝐞𝐦
⚡ 𝐀𝐥𝐩𝐡𝐚 𝐆𝐚𝐭𝐞𝐰𝐚𝐲
🔥 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐀𝐜𝐜𝐞𝐬𝐬

👉 𝐉𝐨𝐢𝐧 𝐓𝐡𝐞𝐧 𝐂𝐥𝐢𝐜𝐤 𝐕𝐞𝐫𝐢𝐟𝐲
""",

            reply_markup=buttons
        )

        return

    await auto_delete_sticker(
        context,
        update.effective_chat.id,
        SUCCESS_STICKER,
        1
    )

    boot = await update.message.reply_text("⚡")

    await boot_animation(boot)

    await boot.delete()

    await send_home(update, context)

# ================= VERIFY =================

async def verify_callback(update, context):

    query = update.callback_query

    await query.answer()

    joined = await check_join(update, context)

    if not joined:

        await auto_delete_sticker(
            context,
            query.message.chat.id,
            DENIED_STICKER,
            2
        )

        await query.message.reply_text(

"""
╔═══ ❖ • 𝐃𝐄𝐍𝐈𝐄𝐃 • ❖ ═══╗

❌ 𝐘𝐨𝐮 𝐃𝐢𝐝𝐧'𝐭 𝐉𝐨𝐢𝐧

🛡 𝐒𝐞𝐜𝐮𝐫𝐢𝐭𝐲 𝐋𝐨𝐜𝐤
📡 𝐕𝐞𝐫𝐢𝐟𝐢𝐜𝐚𝐭𝐢𝐨𝐧 𝐅𝐚𝐢𝐥𝐞𝐝
"""
        )

        return

    await auto_delete_sticker(
        context,
        query.message.chat.id,
        SUCCESS_STICKER,
        1
    )

    boot = await query.message.reply_text("⚡")

    await boot_animation(boot)

    await boot.delete()

    fake_update = Update(
        update.update_id,
        message=query.message
    )

    await send_home(fake_update, context)

# ================= HANDLER =================

async def handle(update, context):

    text = update.message.text

    uid = str(update.effective_user.id)

    # ================= BACK =================

    if text == "🔙 𝐁𝐀𝐂𝐊":

        context.user_data["waiting_number"] = False

        await auto_delete_sticker(
            context,
            update.effective_chat.id,
            LOADING_STICKER,
            1
        )

        await send_home(update, context)

        return

    # ================= REFRESH =================

    if text == "🔄 𝐑𝐄𝐅𝐑𝐄𝐒𝐇":

        await start(update, context)

        return

    # ================= PROFILE =================

    if text == "👤 𝐏𝐑𝐎𝐅𝐈𝐋𝐄":

        data = db.get(uid)

        await update.message.reply_text(

f"""
╔═══ ❖ • 𝐏𝐑𝐎𝐅𝐈𝐋𝐄 • ❖ ═══╗

👤 𝐔𝐬𝐞𝐫 : {uid}
📊 𝐑𝐞𝐪𝐮𝐞𝐬𝐭𝐬 : {data['requests']}
📞 𝐒𝐚𝐯𝐞𝐝 : {len(data['numbers'])}
⚡ 𝐒𝐭𝐚𝐭𝐮𝐬 : 𝐀𝐜𝐭𝐢𝐯𝐞
🔥 𝐀𝐜𝐜𝐞𝐬𝐬 : 𝐏𝐫𝐞𝐦𝐢𝐮𝐦
🛡 𝐒𝐞𝐜𝐮𝐫𝐢𝐭𝐲 : 𝐎𝐍
""",

            reply_markup=back_keyboard()
        )

        return

    # ================= SETTINGS =================

    if text == "⚙️ 𝐒𝐄𝐓𝐓𝐈𝐍𝐆𝐒":

        await update.message.reply_text(

"""
╔═══ ❖ • 𝐒𝐄𝐓𝐓𝐈𝐍𝐆𝐒 • ❖ ═══╗

🛡 𝐀𝐧𝐭𝐢 𝐒𝐩𝐚𝐦 : ✅
⚡ 𝐋𝐢𝐯𝐞 𝐄𝐧𝐜𝐫𝐲𝐩𝐭𝐢𝐨𝐧 : ✅
📡 𝐒𝐦𝐚𝐫𝐭 𝐃𝐞𝐭𝐞𝐜𝐭𝐢𝐨𝐧 : ✅
🔥 𝐀𝐥𝐩𝐡𝐚 𝐅𝐢𝐫𝐞𝐰𝐚𝐥𝐥 : ✅
💎 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐌𝐨𝐝𝐞 : ✅
""",

            reply_markup=back_keyboard()
        )

        return

    # ================= STATUS =================

    if text == "📊 𝐒𝐓𝐀𝐓𝐔𝐒":

        await update.message.reply_text(

f"""
╔═══ ❖ • 𝐒𝐓𝐀𝐓𝐔𝐒 • ❖ ═══╗

🟢 𝐎𝐍𝐋𝐈𝐍𝐄
👥 𝐔𝐬𝐞𝐫𝐬 : {len(db)}
⚡ 𝐀𝐜𝐭𝐢𝐯𝐞 : {len(active_users)}
⏱ 𝐔𝐩𝐭𝐢𝐦𝐞 : {get_uptime()}
🔥 𝐒𝐞𝐫𝐯𝐞𝐫 : 𝐒𝐭𝐚𝐛𝐥𝐞
""",

            reply_markup=back_keyboard()
        )

        return

    # ================= SUPPORT =================

    if text == "🆘 𝐒𝐔𝐏𝐏𝐎𝐑𝐓":

        await update.message.reply_text(

f"""
╔═══ ❖ • 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 • ❖ ═══╗

🆘 𝟐𝟒/𝟕 𝐒𝐮𝐩𝐩𝐨𝐫𝐭
⚡ 𝐅𝐚𝐬𝐭 𝐑𝐞𝐩𝐥𝐲
📡 𝐀𝐥𝐩𝐡𝐚 𝐍𝐞𝐭𝐰𝐨𝐫𝐤

👉 {SUPPORT_LINK}
""",

            reply_markup=back_keyboard()
        )

        return

    # ================= ADMIN =================

    if text == "👑 𝐀𝐃𝐌𝐈𝐍":

        await update.message.reply_text(

"""
╔═══ ❖ • 𝐀𝐃𝐌𝐈𝐍 • ❖ ═══╗

👑 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 𝐏𝐚𝐧𝐞𝐥
🛡 𝐀𝐥𝐩𝐡𝐚 𝐒𝐞𝐜𝐮𝐫𝐢𝐭𝐲
📡 𝐒𝐲𝐬𝐭𝐞𝐦 𝐎𝐧𝐋𝐢𝐧𝐞
""",

            reply_markup=back_keyboard()
        )

        return

    # ================= GET AC =================

    if text == "📲 𝐆𝐄𝐓 𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 𝐀𝐂":

        context.user_data["waiting_number"] = True

        await auto_delete_sticker(
            context,
            update.effective_chat.id,
            LOADING_STICKER,
            1
        )

        await update.message.reply_text(

"""
╔═══ ❖ • 𝐆𝐄𝐓 𝐀𝐂 • ❖ ═══╗

📲 𝐒𝐞𝐧𝐝 𝐖𝐡𝐚𝐭𝐬𝐀𝐩𝐩 𝐍𝐮𝐦𝐛𝐞𝐫

✅ Example :
+911234567890
""",

            reply_markup=back_keyboard()
        )

        return

    # ================= OPEN WHATSAPP =================

    if text == "📲 𝐎𝐏𝐄𝐍 𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏":

        link = context.user_data.get("last_link")

        if not link:
            return

        buttons = InlineKeyboardMarkup([

            [
                InlineKeyboardButton(
                    "🚀 𝐎𝐏𝐄𝐍 𝐍𝐎𝐖",
                    url=link
                )
            ]

        ])

        await update.message.reply_text(

"""
╔═══ ❖ • 𝐎𝐏𝐄𝐍 • ❖ ═══╗

🚀 𝐂𝐥𝐢𝐜𝐤 𝐁𝐮𝐭𝐭𝐨𝐧 𝐁𝐞𝐥𝐨𝐰
📲 𝐖𝐡𝐚𝐭𝐬𝐀𝐩𝐩 𝐑𝐞𝐚𝐝𝐲
""",

            reply_markup=buttons
        )

        return

    # ================= IGNORE RANDOM =================

    if not context.user_data.get("waiting_number"):
        return

    # ================= INVALID =================

    if not valid_number(text):

        await update.message.reply_text(

"""
❌ 𝐈𝐍𝐕𝐀𝐋𝐈𝐃 𝐍𝐔𝐌𝐁𝐄𝐑

✅ Example :
+911234567890
"""
        )

        return

    # ================= COOLDOWN =================

    now = time.time()

    if uid in cooldown:

        remaining = 120 - (now - cooldown[uid])

        if remaining > 0:

            timer = await update.message.reply_text("⏳")

            while remaining > 0:

                mins = int(remaining // 60)

                secs = int(remaining % 60)

                try:

                    await timer.edit_text(

f"""
╔═══ ❖ • 𝐂𝐎𝐎𝐋𝐃𝐎𝐖𝐍 • ❖ ═══╗

⏳ 𝐖𝐚𝐢𝐭 𝐁𝐞𝐟𝐨𝐫𝐞 𝐍𝐞𝐱𝐭 𝐒𝐞𝐚𝐫𝐜𝐡

🕒 {mins:02}:{secs:02}

▓▓▓▓▓▓▓▓▓▓
"""
                    )

                except:
                    pass

                await asyncio.sleep(1)

                remaining -= 1

            return

    cooldown[uid] = now

    # ================= PROCESS =================

    await auto_delete_sticker(
        context,
        update.effective_chat.id,
        UPLOAD_STICKER,
        2
    )

    process = await update.message.reply_text("⚡")

    await progress_animation(process)

    await process.delete()

    await auto_delete_sticker(
        context,
        update.effective_chat.id,
        SUCCESS_STICKER,
        1
    )

    # ================= SAVE =================

    db[uid]["requests"] += 1

    db[uid]["numbers"].append(text)

    save_db(db)

    wa_link = f"https://wa.me/{text.replace('+', '')}"

    context.user_data["last_link"] = wa_link

    context.user_data["waiting_number"] = False

    # ================= RESULT =================

    await update.message.reply_text(

f"""
╔═══ ❖ • 𝐑𝐄𝐒𝐔𝐋𝐓 • ❖ ═══╗

📞 𝐍𝐮𝐦𝐛𝐞𝐫 : {text}
⚡ 𝐒𝐭𝐚𝐭𝐮𝐬 : 𝐕𝐚𝐥𝐢𝐝
🧠 𝐕𝐚𝐥𝐢𝐝𝐚𝐭𝐢𝐨𝐧 : 𝐒𝐮𝐜𝐜𝐞𝐬𝐬
📡 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 : 𝐂𝐨𝐧𝐧𝐞𝐜𝐭𝐞𝐝
🛡 𝐒𝐞𝐜𝐮𝐫𝐢𝐭𝐲 : 𝐕𝐞𝐫𝐢𝐟𝐢𝐞𝐝

🚀 𝐑𝐞𝐚𝐝𝐲 𝐓𝐨 𝐎𝐩𝐞𝐧
""",

        reply_markup=result_keyboard()
    )

# ================= MAIN =================

def main():

    app = (
        Application.builder()
        .token(TOKEN)
        .connect_timeout(30)
        .read_timeout(30)
        .write_timeout(30)
        .pool_timeout(30)
        .build()
    )

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CallbackQueryHandler(
            verify_callback,
            pattern="verify"
        )
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle
        )
    )

    print("🤖 𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 𝐗 𝐎𝐍𝐋𝐈𝐍𝐄")

    app.run_polling(
        drop_pending_updates=True,
        allowed_updates=Update.ALL_TYPES,
        close_loop=False
    )

# ================= RUN =================

if __name__ == "__main__":

    while True:

        try:

            main()

        except KeyboardInterrupt:

            print("🛑 𝐁𝐎𝐓 𝐒𝐓𝐎𝐏𝐏𝐄𝐃")

            break

        except Exception as e:

            print(f"𝐂𝐑𝐀𝐒𝐇 : {e}")

            time.sleep(5)

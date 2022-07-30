import random, os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


Bot = Client(
    "Password Generator Bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)

TEXT = """**Hai {},
Merhaba Ben Şifre Üretici Bot. İstediğin Uzunlukta Güçlü Şifre Oluşturabilirim (Max. 84).**

Daha Fazla Bilgi İçin /help"""

BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Kanal 🔰", url = "https://t.me/SancakBotlar"),
            InlineKeyboardButton("Support Grup ⭕️", url = "https://t.me/muhabbetofkings")
        ],
        [
            InlineKeyboardButton("Sahip 👮‍♂️", url = "https://t.me/sancakbegi"),
            InlineKeyboardButton("Arşiv Kanalımız ⚡", url = "https://t.me/CyberTurkish")
        ],
        [
            InlineKeyboardButton("Developer 💡", url = "https://t.me/sancakbegi")
        ]
    ]
)

HELP = """Merhaba {},
**Daha Fazla Bilgi.**

- Bana Şifrelerin veya anahtarların limitini gönder (isteğe bağlı)
  Like :-
    `10 abcd1234`
    `10`
- Bu limitin Şifresini vereceğim.

**Not :-**
• Sadece Rakamlara İzin Verilir
• İzin Verilen Maksimim Rakam 100 ( 84 Uzunluğunun Üzerinde Şifre Oluşturamıyorum)"""

HELP_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🧑‍💻 KANAL", url = "https://telegram.me/SancakBotlar"),
            InlineKeyboardButton("👮‍♂️ DEVELOPER", url = "https://t.me/sancakbegi")
        ]
    ]
)

ABOUT = """--**🇹🇷Benim Hakkımda🇹🇷**--

**🤖 Bot :** Sancak Şifre Üretici Bot
**🧑‍💻 Developer :** [SancakBegi](https://t.me/SancakBegi)
**💻 Kanal :** @SancakBotlar
**☎️ Support :** @muhabbetofkingd
**🗂️ Arşiv Kanalımız :** [Cyber Turkish](https://t.me/CyberTurkish)
**⚙️ Dil :** Python 3
**🛡️ Framework :** Pyrogram"""


@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=TEXT.format(update.from_user.mention),
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )


@Bot.on_message(filters.private & filters.command(["help"]))
async def help(bot, update):
    await update.reply_text(
        text=HELP.format(update.from_user.mention),
        reply_markup=HELP_BUTTON,
        disable_web_page_preview=True,
        quote=True
    )


@Bot.on_message(filters.private & filters.command(["about", "source", "repo"]))
async def about(bot, update):
    await update.reply_text(
        text=ABOUT,
        disable_web_page_preview=True,
        quote=True
    )


@Bot.on_message(filters.private & filters.text)
async def password(bot, update):
    
    message = await message.reply_text('`Processing...`')
    
    try:
        if len(update.text.split()) > 1:
            keys, limit = update.text.split()[1], int(update.text.split()[0])
        else:
            keys = "abcdefghijklmnopqrstuvwxyz"+"1234567890"+"!@#$%^&*()_+".lower()
            limit = int(update.text)
    except:
        await message.edit_text('Something wrong')
        return
    
    if limit > 100 or limit <= 0:
        text = "Üzgünüm... Şifre Üretilirken Hata Oluştu, çünkü limit 1 ile 100 arasında olduğu için "
    else:
        random_value = "".join(random.sample(password, limit))
        text = f"**Limit :-** `{str(limit)}`.\n**Password :-** `{random_value}`**\n\nJoin @SancakBotlar"
    
    await message.edit_text(text, True)


Bot.run()

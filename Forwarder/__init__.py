import os
from pyrogram import Client, filters, idle
from pyromod import listen
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from telethon import TelegramClient
from telethon.sessions import StringSession
import logging
from logging.handlers import RotatingFileHandler

ENV = os.environ.get('ENV', None)

if ENV:
    from BotConfig import Config
else:
    from local_config import Development as Config

APP_ID = Config.API_ID
API_HASH = Config.API_HASH
TG_BOT_WORKERS = 4
BOT_TOKEN = Config.BOT_TOKEN
STRING_SESSION = Config.STRING_SESSION
SUDO_USERS = Config.SUDO_USERS
DB_URL = Config.DB_URI

if DB_URL.startswith('postgres://'):
    DB_URL = DB_URL.replace('postgres', 'postgresql', 1)

SUDO_IDS = SUDO_USERS.split(' ')


def is_sudo(_, client, update):
    try:
        user_id = update.from_user.id
    except:
        return False
    if str(user_id) in SUDO_IDS:
        return True
    else:
        return False


filters.admins = filters.create(is_sudo)

LOG_FILE_NAME = "codexbotz.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)


# ----------CLIENT----------- #

client = TelegramClient(StringSession(STRING_SESSION), APP_ID, API_HASH)
client.start()


# -----------BOT------------- #

class Bot(Client):
    def __init__(self):
        super().__init__(
            "Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "Forwarder/plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=BOT_TOKEN
        )
        self.LOGGER = LOGGER


    async def start(self):
        await super().start()
        bot_details = await self.get_me()
        self.LOGGER(__name__).info(f"@{bot_details.username}  started!")
        self.LOGGER(__name__).info("Created by CODE X BOTZ \nhttps://t.me/Bot")
        self.bot_details = bot_details
        self.client = client
        await client.send_message(bot_details.username,'/check')


    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
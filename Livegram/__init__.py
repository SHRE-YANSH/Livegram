import os
from telethon import TelegramClient
import logging
from telegram.ext import Updater, CommandHandler, Dispatcher

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO)
    
LOGGER = logging.getLogger(__name__)

class Config(object):
    LOGGER = True
    # Get this value from my.telegram.org! Please do not steal
    API_ID = int(os.environ.get("API_ID", None))
    API_HASH = os.environ.get("API_HASH", "")
    TOKEN = os.environ.get("TOKEN", "")
    SUDO_USERS = [919262859, 552861144, 585145887, 698297764, 1245831019]  
    CHAT_ID = os.environ.get("CHAT_ID", "")

class Production(Config):
    LOGGER = False

class Development(Config):
    LOGGER = True

bot = TelegramClient('for', Config.API_ID, Config.API_HASH).start(bot_token=Config.TOKEN)
updater = Updater(Config.TOKEN, use_context=True)
dispatcher = updater.dispatcher

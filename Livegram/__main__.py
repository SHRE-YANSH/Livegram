import importlib
from Livegram import dispatcher, updater, Config, bot, dispatcher, LOGGER
from Livegram.mod import ALL_MODULES
from telegram import Message, Update, Bot, User
from telegram.ext import (CallbackContext, CallbackQueryHandler, CommandHandler,
                          Filters, MessageHandler, run_async)
from telegram import ParseMode      
           
IMPORTED = {}
MIGRATEABLE = []
HELPABLE = {}
STATS = []
USER_INFO = []
DATA_IMPORT = []
DATA_EXPORT = []

CHAT_SETTINGS = {}
USER_SETTINGS = {}

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("Livegram.mod." + module_name)
    if not hasattr(imported_module, "__mod_name__"):
        imported_module.__mod_name__ = imported_module.__name__

    if not imported_module.__mod_name__.lower() in IMPORTED:
        IMPORTED[imported_module.__mod_name__.lower()] = imported_module
    else:
        raise Exception("Can't have two modules with the same name! Please change one")

    if hasattr(imported_module, "__help__") and imported_module.__help__:
        HELPABLE[imported_module.__mod_name__.lower()] = imported_module

    # Chats to migrate on chat_migrated events
    if hasattr(imported_module, "__migrate__"):
        MIGRATEABLE.append(imported_module)

    if hasattr(imported_module, "__stats__"):
        STATS.append(imported_module)

    if hasattr(imported_module, "__user_info__"):
        USER_INFO.append(imported_module)

    if hasattr(imported_module, "__import_data__"):
        DATA_IMPORT.append(imported_module)

    if hasattr(imported_module, "__export_data__"):
        DATA_EXPORT.append(imported_module)

    if hasattr(imported_module, "__chat_settings__"):
        CHAT_SETTINGS[imported_module.__mod_name__.lower()] = imported_module

    if hasattr(imported_module, "__user_settings__"):
        USER_SETTINGS[imported_module.__mod_name__.lower()] = imported_module
        
@run_async
def start(update, context):
	user = update.message.from_user
	if update.effective_message.chat.type == "private":
	    text = "Official Bot for @BruteForcers Send it feedbacks or any config requests here to be done.ԅ( ͒ ۝ ͒ )ᕤ."
	else:
            text = "What bsdk?"
	update.effective_message.reply_text(text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)

def main():
    test_handler = CommandHandler("start", start)
    dispatcher.add_handler(test_handler)
    updater.start_polling()
    bot.run_until_disconnected()

if __name__ == '__main__':
    LOGGER.info("Successfully loaded modules: " + str(ALL_MODULES))
    bot
    main()

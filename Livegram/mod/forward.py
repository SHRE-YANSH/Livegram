import logging
import os
from Livegram import updater, dispatcher, Config
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import ParseMode

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

to_c = Config.CHAT_ID
if os.isfile(blacklist.txt):
    f = open('blacklist.txt', 'r+')
    BL_CHAT = f.read().splitlines()
    f.close()
def forward(update, context):
    user = update.message.from_user
    if user['id'] in BL_CHAT:
         update.effective_message.reply_text("You have been blocked")
         return
    if not update.effective_message.chat.type == "private":
    	return
    context.bot.forward_message(chat_id=to_c,
                        from_chat_id=update.message.chat_id,
                        message_id=update.message.message_id)
    context.bot.send_message(chat_id=to_c, text=f"{user['first_name']} id is `{user['id']}`", parse_mode=ParseMode.MARKDOWN_V2)
                        
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, forward))

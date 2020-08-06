import logging
from Livegram import updater, dispatcher, Config
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

to_c = Config.CHAT_ID

def forward(update, context):
    if not update.effective_message.chat.type == "private":
    	return
    context.bot.forward_message(chat_id=to_c,
                        from_chat_id=update.message.chat_id,
                        message_id=update.message.message_id)
                        
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, forward))

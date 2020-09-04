import logging
import os
from Livegram import updater, dispatcher, Config
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import ParseMode
from Livegram.mod.sql.blacklist_sql import check_is_black_list

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

to_c = Config.CHAT_ID


def forward(update, context):
    user = update.message.from_user
    check_ban = check_is_black_list(user['id'])
    if check_ban:
       context.bot.send_message(chat_id=user['id'], text="You have been banned.")
       return
    message = update.message
    if not update.effective_message.chat.type == "private":
    	return
    context.bot.forward_message(chat_id=to_c,
                        from_chat_id=update.message.chat_id,
                        message_id=update.message.message_id)
    context.bot.send_message(chat_id=to_c, text=f"{user['first_name']} id is `{user['id']}`", parse_mode=ParseMode.MARKDOWN_V2)
                  
dispatcher.add_handler(MessageHandler(Filters.all & ~Filters.command, forward))

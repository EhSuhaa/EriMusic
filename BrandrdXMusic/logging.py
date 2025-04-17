from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from BrandrdXMusic import application
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        logging.FileHandler("log.txt"),
        logging.StreamHandler(),
    ],
)

logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)
logging.getLogger("pymongo").setLevel(logging.ERROR)
logging.getLogger("ntgcalls").setLevel(logging.ERROR)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

LOGGING_CHAT_ID = "YOUR_CHAT_ID"

def log_ban_kick(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.username
    action = "Ban/Kick"
    target_user_id = update.message.new_chat_member.id
    log_message = f"{user_name} (ID: {user_id}) {action}ed {target_user_id}"
    LOGGER("admin_actions").info(log_message)
    context.bot.send_message(chat_id=LOGGING_CHAT_ID, text=log_message)
    with open("admin_actions.log", "a") as file:
        file.write(f"{log_message}\n")

def log_promotion(update: Update, context: CallbackContext):
    promoted_user_id = update.message.new_chat_member.id
    action = "Promoted"
    log_message = f"User {promoted_user_id} was {action} to admin."
    LOGGER("admin_actions").info(log_message)
    context.bot.send_message(chat_id=LOGGING_CHAT_ID, text=log_message)
    with open("admin_actions.log", "a") as file:
        file.write(f"{log_message}\n")



    application.add_handler(MessageHandler(Filters.status_update.new_chat_members, log_ban_kick))
    application.add_handler(MessageHandler(Filters.status_update.left_chat_member, log_ban_kick))
    application.add_handler(MessageHandler(Filters.status_update.promoted_chat_member, log_promotion))

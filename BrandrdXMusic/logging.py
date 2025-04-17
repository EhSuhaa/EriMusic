import logging
from pyrogram import filters
from pyrogram.types import Message
from BrandrdXMusic import *

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

 

@app.on_message(filters.new_chat_members)
def log_ban_kick(client, message: Message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    action = "Ban/Kick"
    target_user_id = message.new_chat_members[0].id
    log_message = f"{user_name} (ID: {user_id}) {action}ed {target_user_id}"
    LOGGER("admin_actions").info(log_message)
    client.send_message(chat_id=LOGGING_CHAT_ID, text=log_message)
    with open("admin_actions.log", "a") as file:
        file.write(f"{log_message}\n")

@app.on_message(filters.left_chat_member)
def log_ban_kick_left(client, message: Message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    action = "Ban/Kick"
    target_user_id = message.left_chat_member.id
    log_message = f"{user_name} (ID: {user_id}) {action}ed {target_user_id}"
    LOGGER("admin_actions").info(log_message)
    client.send_message(chat_id=LOGGING_CHAT_ID, text=log_message)
    with open("admin_actions.log", "a") as file:
        file.write(f"{log_message}\n")

@app.on_message(filters.promoted_chat_member)
def log_promotion(client, message: Message):
    promoted_user_id = message.promoted_chat_member.id
    action = "Promoted"
    log_message = f"User {promoted_user_id} was {action} to admin."
    LOGGER("admin_actions").info(log_message)
    client.send_message(chat_id=LOGGING_CHAT_ID, text=log_message)
    with open("admin_actions.log", "a") as file:
        file.write(f"{log_message}\n")

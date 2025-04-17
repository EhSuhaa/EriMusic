import logging
from pyrogram import filters
from pyrogram.types import Message
from BrandrdXMusic import app

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

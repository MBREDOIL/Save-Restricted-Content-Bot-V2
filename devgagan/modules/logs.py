from pyrogram import Client, filters
from pyrogram.types import Message
from config import API_ID, API_HASH, BOT_TOKEN

LOG_GROUP = '-1002227803088'

apy = Client(
    "Res",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN)

    
@apy.on_message(filters.text)
async def log_user(update: Message):
    user = update.from_user
    user_name = user.first_name
    user_id = user.id
    
    # Use .mention to get the proper mention format (works even without a username)
    user_mention = user.mention
    
    # Log the user's details to the log channel
    log_message = (f"User interacted with bot: {user_name} ({user_mention})\n"
                   f"User ID: {user_id}\n"
                   f"Message: {update.text}")
    
    # Ensure to await the asynchronous operation of sending the log message
    await apy.send_message(chat_id=LOG_GROUP, text=log_message)
    

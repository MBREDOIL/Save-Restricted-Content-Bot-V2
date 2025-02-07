from pyrogram import Client, filters
from pyrogram.types import Message
from config import API_ID, API_HASH, BOT_TOKEN

LOG_GROUP = '-1002227803088'

app = Client(
    "Res",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN)

    
@app.on_message(filters.text)
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
    await app.send_message(chat_id=LOG_GROUP, text=log_message)





@app.on_message(filters.command("dp") & filters.private)
async def get_profile_photo(client: Client, message: Message):
    # Extract the user ID from the command
    if len(message.command) < 2:
        await message.reply_text("Please provide a user ID. Usage: /dp <user_id>")
        return
    
    user_id = int(message.command[1])

    try:
        # Fetch all profile photos of the specified user
        profile_photos = await client.get_profile_photos(user_id)

        if not profile_photos:
            await message.reply_text("This user has no profile photos.")
            return

        # Send all profile photos to the same chat
        for photo in profile_photos:
            await client.send_photo(chat_id=message.chat.id, photo=photo.file_id)

    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")

app.run()

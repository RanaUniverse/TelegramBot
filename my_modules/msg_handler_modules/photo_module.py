'''
This function handles processing for received photo updates.
The import of this function is:
from my_modules.msg_handler_modules.photo_module import photo_received_update
'''

from telegram import Update
from telegram.ext import ContextTypes

async def photo_received_update(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This function sends the user details of the received photo update.'''
    user = update.message.from_user
    photo = update.message.photo[-1]  # Considering only the last (highest resolution) photo

    # Extracting photo details
    file_id = photo.file_id
    file_unique_id = photo.file_unique_id
    width = photo.width
    height = photo.height
    file_size = photo.file_size

    # Creating a message with the extracted photo information
    message = (
        f"📷 Photo Information:\n"
        f"🆔 File ID: {file_id}\n"
        f"🔖 Unique ID: {file_unique_id}\n"
        f"📏 Width: {width}px\n"
        f"📐 Height: {height}px\n"
        f"📦 File Size: {file_size} bytes\n"
    )

    # Sending the message back to the user
    await context.bot.send_message(user.id, message)

    # Optionally, log that the photo information was sent
    print(f"Photo information sent for user: {user.id}")

# Then, add a handler for the photo message
# application.add_handler(MessageHandler(filters=filters.Photo, callback=photo_received_update))

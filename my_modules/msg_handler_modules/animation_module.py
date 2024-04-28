'''
This will help to handle different animation processing function
these function will call other fun on how to edit images
The import of this function is:
from my_modules.msg_handler_modules.animation_module import animation_received_update


Usage:
    application.add_handler(MessageHandler(
        filters=filters.ANIMATION,
        callback=animation_received_update,
        block=False
    ))
'''


from telegram import Update
from telegram.ext import ContextTypes

async def animation_received_update(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This function sends the user the details of the received animation update.'''
    user = update.message.from_user
    animation = update.message.animation

    file_id = animation.file_id
    file_unique_id = animation.file_unique_id
    width = animation.width
    height = animation.height
    duration = animation.duration
    thumbnail = animation.thumbnail  
    file_name = animation.file_name
    mime_type = animation.mime_type
    file_size = animation.file_size

    message = (
        f"🎬 Animation Information:\n"
        f"🆔 File ID: {file_id}\n"
        f"🔖 Unique ID: {file_unique_id}\n"
        f"📏 Width: {width}px\n"
        f"📐 Height: {height}px\n"
        f"⏱ Duration: {duration} seconds\n"
        f"📁 File Name: {file_name}\n"
        f"📝 MIME Type: {mime_type}\n"
        f"📦 File Size: {file_size} bytes\n"
        f"🖼️ Thumbnail: {thumbnail}\n"
    )

    await context.bot.send_message(user.id, message)

    # Optionally, you can download the thumbnail using await thumbnail.download()
    # This will save the thumbnail locally, and you can then process or use it as needed

    # Optionally, log that the animation information was sent
    print(f"Animation information sent for user: {user.id}")

# Then, add a handler for the animation message
# application.add_handler(MessageHandler(filters=filters.Animation, callback=animation_received_update))

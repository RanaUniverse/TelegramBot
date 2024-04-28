'''
This function handles processing for received audio updates.
The import of this function is:
from my_modules.msg_handler_modules.audio_module import audio_received_update
'''

from telegram import Update
from telegram.ext import ContextTypes

async def audio_received_update(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This function sends the user details of the received audio update.'''
    user = update.message.from_user
    audio = update.message.audio

    # Extracting audio details
    file_id = audio.file_id
    file_unique_id = audio.file_unique_id
    duration = audio.duration
    performer = audio.performer if audio.performer else "Unknown"
    title = audio.title if audio.title else "Untitled"
    file_name = audio.file_name if audio.file_name else "Untitled"
    mime_type = audio.mime_type if audio.mime_type else "audio/mpeg"
    file_size = audio.file_size if audio.file_size else 0
    thumbnail = audio.thumbnail  # This will be a PhotoSize object

    # Creating a message with the extracted audio information
    message = (
        f"🎵 Audio Information:\n"
        f"🆔 File ID: {file_id}\n"
        f"🔖 Unique ID: {file_unique_id}\n"
        f"⏱ Duration: {duration} seconds\n"
        f"🎤 Performer: {performer}\n"
        f"📝 Title: {title}\n"
        f"📁 File Name: {file_name}\n"
        f"📝 MIME Type: {mime_type}\n"
        f"📦 File Size: {file_size} bytes\n"
        f"🖼️ Thumbnail: {thumbnail}\n"
    )

    # Sending the message back to the user
    await context.bot.send_message(user.id, message)

    # Optionally, you can download the thumbnail using await thumbnail.download()
    # This will save the thumbnail locally, and you can then process or use it as needed

    # Optionally, log that the audio information was sent
    print(f"Audio information sent for user: {user.id}")

# Then, add a handler for the audio message
# application.add_handler(MessageHandler(filters=filters.Audio, callback=audio_received_update))

"""
This module contains the handler function for processing received Sticker messages.

Usage:

    application.add_handler(MessageHandler(
        filters=filters.Sticker.ALL,
        callback=sticker_received_update,
        block=False
    ))

The handler function `sticker_received_update` processes received Sticker messages and sends back information about the sticker.
"""


from telegram import Update
from telegram.ext import ContextTypes


async def sticker_received_update(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    sticker = update.message.sticker

    # Extracting sticker details
    file_id = sticker.file_id
    file_unique_id = sticker.file_unique_id
    sticker_type = sticker.type
    width = sticker.width
    height = sticker.height
    is_animated = sticker.is_animated
    is_video = sticker.is_video
    thumbnail = sticker.thumbnail  # This will be a PhotoSize object
    emoji = sticker.emoji
    set_name = sticker.set_name
    premium_animation = sticker.premium_animation
    mask_position = sticker.mask_position
    custom_emoji_id = sticker.custom_emoji_id
    needs_repainting = sticker.needs_repainting
    file_size = sticker.file_size

    # Creating a message with the extracted sticker information
    message = (
        f"🎨 Sticker Information:\n"
        f"🆔 File ID: {file_id}\n"
        f"🔖 Unique ID: {file_unique_id}\n"
        f"🏷️ Type: {sticker_type}\n"
        f"📏 Width: {width}\n"
        f"📐 Height: {height}\n"
        f"🔄 Animated: {is_animated}\n"
        f"📹 Video Sticker: {is_video}\n"
        f"🖼️ Thumbnail: {thumbnail}\n"
        f"😀 Emoji: {emoji}\n"
        f"🖼️ Set Name: {set_name}\n"
        f"💎 Premium Animation: {premium_animation}\n"
        f"🎭 Mask Position: {mask_position}\n"
        f"🆔 Custom Emoji ID: {custom_emoji_id}\n"
        f"🎨 Needs Repainting: {needs_repainting}\n"
        f"📦 File Size: {file_size} bytes\n"
    )

    # Sending the message back to the user
    await context.bot.send_message(user.id, message)

    # Optionally, you can download the thumbnail using await thumbnail.download()
    # This will save the thumbnail locally, and you can then process or use it as needed

    # Optionally, log that the sticker information was sent
    print(f"Sticker information sent for user: {user.id}")

    # Adding the handler for sticker messages
    # application.add_handler(MessageHandler(filters=filters.STICKER, callback=sticker_received_update, block=False))

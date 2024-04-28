'''
This will help to handle different dice processing function
these function will call other fun on how to edit images
The import of this function is:
from my_modules.msg_handler_modules.dice_module import dice_received_update

Usage:
    application.add_handler(MessageHandler(
        filters=filters.Dice.ALL,
        callback=dice_received_update,
        block=False
    ))
'''


from telegram import Update
from telegram.ext import ContextTypes

async def dice_received_update(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This function sends the user the details of the received dice information.'''
    user = update.message.from_user
    dice = update.message.dice

    # Extracting dice details
    emoji = dice.emoji
    value = dice.value

    # Creating a message with the extracted dice information
    message = (
        f"🎲 Dice Information:\n"
        f"🎯 Emoji: {emoji}\n"
        f"🎲 Value: {value}"
    )

    # Sending the message back to the user
    await context.bot.send_message(user.id, message)

    # Optionally, you can do further processing with the dice data

    # Optionally, log that the dice information was sent
    print(f"Dice information sent for user: {user.id}")

# Then, add a handler for the dice message
# application.add_handler(MessageHandler(filters=filters.Dice, callback=dice_received_update))

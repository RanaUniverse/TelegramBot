'''
This will help to handle different contact processing function
these function will call other fun on how to edit images
The import of this function is:
from my_modules.msg_handler_modules.contact_module import contact_received_update

Usage:
    application.add_handler(MessageHandler(
        filters=filters.CONTACT,
        callback=contact_received_update,
        block=False
    ))
'''


from telegram import Update
from telegram.ext import ContextTypes

async def contact_received_update(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This function sends the user the details of the received contact information.'''
    user = update.message.from_user
    contact = update.message.contact

    # Extracting contact details
    phone_number = contact.phone_number
    first_name = contact.first_name
    last_name = contact.last_name if contact.last_name else ""
    user_id = contact.user_id if contact.user_id else ""
    vcard = contact.vcard if contact.vcard else ""

    # Creating a message with the extracted contact information
    message = (
        f"📞 Contact Information:\n"
        f"📱 Phone Number: {phone_number}\n"
        f"👤 First Name: {first_name}\n"
        f"👥 Last Name: {last_name}\n"
        f"🆔 User ID: {user_id}\n"
        f"📇 vCard: {vcard}"
    )

    # Sending the message back to the user
    await context.bot.send_message(user.id, message)

    # Optionally, you can do further processing with the contact data

    # Optionally, log that the contact information was sent
    print(f"Contact information sent for user: {user.id}")

# Then, add a handler for the contact message
# application.add_handler(MessageHandler(filters=filters.Contact, callback=contact_received_update))

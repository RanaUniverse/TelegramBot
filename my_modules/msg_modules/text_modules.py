
'''
in this scripts here i will use some fun which will does from teh text received
** import echo_fun **
** import all_edited_cmd **
** import all_edited_msg **

'''



from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode

print("This bot will run, for any sugesstion please messaage me in my telegram",
      "https://t.me/RanaUniverse")

async def echo_fun(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This will send the same msg send to the bot'''
    user = update.message.from_user
    text = (f"You have send me This Text Below:\n"
            "Thanks Boss")
    await context.bot.send_message(user.id, text)




async def all_edited_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This funciton is execute when any user edit his old msg or cmd to any new /cmd'''
    chat = update.edited_message.chat
    text = update.edited_message.text
    send_text = (f"You have send me:\n<b>{text}</b>"
                 f"Sorry i am not allowed to work on edited msg command"
                 f"Please send me a <code>/command</code> freshly")
    
    await context.bot.send_message(chat.id, text= send_text, parse_mode = ParseMode.HTML)




async def all_edited_msg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''After anyone will edit any msg this will execute'''
    chat = update.edited_message.chat
    text = update.edited_message.text
    send_text = (f"You Have send me {text}"
                 f"I cannot Help you in this edited msg")
    await context.bot.send_message(chat.id, send_text, parse_mode= ParseMode.HTML)




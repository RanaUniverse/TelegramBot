
'''
Here i will defines the functions which i will call directly to exectute
so that it will perform some action when /help will came from user
** import help_cmd **
** import help_cmd_private **
** import help_cmd_group **

Just For Testing For Rana Universe
For Mail: RanaUniverse321@gmail.com
Message Me: https://t.me/RanaUniverse

'''


from telegram import Update

from telegram.ext import ContextTypes



async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = (
        f"This is the HELP Section of this Bot- Rana Universe\n"
        f"To know the capabilities of this Bot Please Press This button"
    )
    await context.bot.send_message(user.id, text)



async def help_cmd_private(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This is from get /help from any priate'''
    user = update.message.from_user
    text = (f"Hello <b>{user.full_name}</b>"
            f"You have send /help, here You can check your details with /start")
    await context.bot.send_message(user.id, text, parse_mode= "html")



async def help_cmd_group(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''This is from get /help from any group'''
    chat = update.message.chat
    text = (f"You want to get help from this go to the private msg not in this:"
            f"<b>{chat.title}</b>")
    await context.bot.send_message(chat.id, text, parse_mode= "html")
    








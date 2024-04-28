
'''
Here i will defines the functions which i will call directly to exectute
so that it will perform some action when /start will came from user

** import start **
** import start_cmd_private **
** import start_cmd_group **
** import start_cmd_channel **

Just For Testing For Rana Universe
For Mail: RanaUniverse321@gmail.com
Message Me: https://t.me/RanaUniverse

'''


from telegram import ForceReply
from telegram import Update
from telegram.ext import ContextTypes



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!\nTHis is any type of chat from start",
        reply_markup=ForceReply(selective=True),
    )



async def start_cmd_private(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    user_bio = (await context.bot.get_chat(user.id)).bio
    text = (
        f"This is Private MSG"
        f"Hello {user.full_name}\n"
        f"Your Bio is:\n<b>{user_bio}</b>"
        f"{await context.bot.get_my_name()}"
    )
    
    await context.bot.send_message(user.id, text, parse_mode= "html")



async def start_cmd_group(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    chat = update.message.chat
    text = (
        f"This is Group MSG"
        f"Hello {chat.title}\n"
        f"You Have Just Started this bot {(await context.bot.get_my_name()).name}:\n"
        f"Send /help to know more on how to use this bot. "
        f"You Need to join our Channel to use our Bot"
    )
    
    await context.bot.send_message(chat.id, text)



async def start_cmd_channel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.channel_post.chat
    name_of_sender = update.channel_post.author_signature

    channel_des = (await context.bot.get_chat(chat.id)).description
    text = (
        f"This is Channel Post For: "
        f"{chat.title}\n"
        f"This has written by <b>{name_of_sender}</b>"
    )
    text += (
        f"Description of This Channel is:\n"
        f"{channel_des}"
    )
    await context.bot.send_message(chat.id, text, parse_mode= "html")







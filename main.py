
'''
This is my main file to run all things are connected mainly with this
The Database System has not implimented Yet

Just For Testing For Rana Universe
Any Sugesstion Please Contact 🍌🍌🍌
For Mail: RanaUniverse321@gmail.com
Message Me: https://t.me/RanaUniverse

'''

import sys
sys.dont_write_bytecode = True



from telegram import Update
from telegram.ext import Application
from telegram.ext import CommandHandler, MessageHandler, filters



from my_modules.abc_modules.bot_config import BOT_TOKEN


from my_modules.cmd_handler_modules.help_module import (
    help_cmd_group,
    help_cmd_private,
    )
    
from my_modules.cmd_handler_modules.start_module import(
    start, 
    start_cmd_channel,
    start_cmd_group,
    start_cmd_private
    )

from my_modules.logger_modules.logger_module import setup_logger


from my_modules.msg_handler_modules import(
    animation_module,
    audio_module,
    contact_module,
    dice_module,
    document_module,
    location_module,
    photo_module,
    sticker_module,
    story_module,
    video_module,
    video_note_module,
    voice_module
    )


from my_modules.msg_modules.text_modules import (echo_fun,
                                                 all_edited_cmd,
                                                 all_edited_msg
                                                 )






'''
Rana Universe 🍌🍌🍌
Rana Universe 🍌🍌🍌
Rana Universe 🍌🍌🍌
Below will my special coding started
Rana Universe 🍌🍌🍌
Rana Universe 🍌🍌🍌
Rana Universe 🍌🍌🍌
'''


logger = setup_logger()




def main() -> None:
    """Start the bot."""

    application = Application.builder().token("Rana Universe Bot Token").build()



    application.add_handler(MessageHandler(
        filters=filters.UpdateType.EDITED & filters.Command(),
        callback=all_edited_cmd,
        block=False
    ))

    application.add_handler(MessageHandler(
        filters=filters.UpdateType.EDITED,
        callback=all_edited_msg,
        block=False
    ))


    application.add_handler(CommandHandler(
        command= ["start", "st"],
        callback= start_cmd_private,
        filters= filters.ChatType.PRIVATE,
        block= False
    ))
    application.add_handler(CommandHandler(
        command= ["start", "st"],
        callback= start_cmd_group,
        filters= filters.ChatType.GROUPS,
        block= False
    ))
    application.add_handler(CommandHandler(
        command= ["start", "st"],
        callback= start_cmd_channel,
        filters= filters.ChatType.CHANNEL,
        block= False
    ))

    application.add_handler(CommandHandler(
        command= ["help", "helps"],
        callback= help_cmd_private,
        filters= filters.ChatType.PRIVATE,
        block= False
    ))
    application.add_handler(CommandHandler(
        command= ["help", "helps"],
        callback= help_cmd_group,
        filters= filters.ChatType.GROUPS,
        block= False
    ))




    application.add_handler(MessageHandler(
        filters=filters.ANIMATION,
        callback=animation_module.animation_received_update,
        block=False
    ))
    application.add_handler(MessageHandler(
        filters=filters.AUDIO,
        callback=audio_module.audio_received_update,
        block=False
    ))
    application.add_handler(MessageHandler(
        filters=filters.CONTACT,
        callback=contact_module.contact_received_update,
        block=False
    ))
    application.add_handler(MessageHandler(
        filters=filters.Dice.ALL,
        callback=dice_module.dice_received_update,
        block=False
    ))
    application.add_handler(MessageHandler(
        filters=filters.Document.ALL,
        callback=document_module.document_received_update,
        block=False
    ))
    application.add_handler(MessageHandler(
        filters=filters.LOCATION,
        callback=location_module.location_received_update,
        block=False
    ))
    application.add_handler(MessageHandler(
        filters=filters.PHOTO,
        callback=photo_module.photo_received_update,
        block=False
    ))
    application.add_handler(MessageHandler(
        filters=filters.Sticker.ALL,
        callback=sticker_module.sticker_received_update,
        block=False
    ))
    application.add_handler(MessageHandler(
        filters=filters.STORY,
        callback=story_module.story_received_update,
        block=False
    ))
    application.add_handler(MessageHandler(
        filters=filters.VIDEO,
        callback=video_module.video_received_update,
        block=False
    ))
    application.add_handler(MessageHandler(
        filters=filters.VIDEO_NOTE,
        callback=video_note_module.video_note_received_update,
        block=False
    ))
    application.add_handler(MessageHandler(
        filters=filters.VOICE,
        callback=voice_module.voice_received_update,
        block=False
    ))










    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_fun))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()








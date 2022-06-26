from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🔗Tap Here for Generate String", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="ʀᴇᴛᴜʀɴ ʜᴏᴍᴇ", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
        ],
    ]

    START = """
Welcome to String Session Generator.
You Can use me for Generate String Sessions.

if you don't have trust you can leave this bot

    """

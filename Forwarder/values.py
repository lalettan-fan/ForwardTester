from pyrogram.types import InlineKeyboardButton

start_text = "<b>Hello {mention}\n\nI am a Forwarder Bot, You can forward files from one channel to another without being admin</b>"
start_text2 = "<b>Hello {mention}\n\nI am a Forwarder Bot, You can forward files from one channel to another without being admin</b>\n\nYou need to deploy your own Bot in-order to forward files"
help_text = "<b>ā Commands available</b>\n\nš· /forward - to forward files from one channel to another\nš· /join - to join a channel from where you need to forward"
about_text = "<b>ABOUT ME</b>\n\n<b>ā Support : <a href='https://t.me/CodeXBotzSupport'>Bot Support</a>\nā Language : <a href='https://www.python.org/'>Python 3</a>\nā Library : <a href='https://github.com/pyrogram/pyrogram'>Pyrogram Asyncio 1.2.9</a>\nā Channel : <a href='https://t.me/CodeXBotz'>Code š Botz</a></b>"

start_keyboard = [
    [
        InlineKeyboardButton(text = 'š¤ Help', callback_data = "help"),
        InlineKeyboardButton(text = 'š¤ About', callback_data = "about")
    ],
    [
        InlineKeyboardButton(text = 'Close š', callback_data = "close")
    ]
]

help_keyboard = [
    [
        InlineKeyboardButton(text = 'š¤ About', callback_data = 'about'),
        InlineKeyboardButton(text = 'Close š', callback_data = 'close')
    ]
]
about_keyboard = [
    [
        InlineKeyboardButton(text = 'š¤ Help', callback_data = 'help'),
        InlineKeyboardButton(text = 'Close š', callback_data = 'close')
    ]
]

repo_keyboard = [
    [
        InlineKeyboardButton(text = 'Repo', url = 'https://github.com/rahulps1000/ForwardBot')
    ],
    [
        InlineKeyboardButton(text = 'Deploy', url = 'https://dashboard.heroku.com/new?button-url=https://github.com/rahulps1000/ForwardBot&template=https://github.com/rahulps1000/ForwardBot')
    ]
]
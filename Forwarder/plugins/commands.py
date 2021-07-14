from Forwarder import Bot,filters,Message,InlineKeyboardMarkup
from Forwarder.values import *

@Bot.on_message(filters.command('start') & filters.private & filters.admins)
async def start(bot: Bot, message: Message):
    await message.reply(
       text = start_text.format(mention=message.from_user.mention),
       quote = True,
       reply_markup = InlineKeyboardMarkup(start_keyboard)
    )
    return

@Bot.on_message(filters.command('start') & filters.private & ~ filters.admins)
async def others(bot: Bot, message: Message):
    await message.reply(
       text = start_text2.format(mention=message.from_user.mention),
       quote = True,
       reply_markup = InlineKeyboardMarkup(repo_keyboard)
    )
    return

@Bot.on_message(filters.command('help') & filters.private)
async def help(bot: Bot, message: Message):
    await message.reply(
       text = help_text,
       quote = True,
       reply_markup = InlineKeyboardMarkup(help_keyboard)
    )
    return

@Bot.on_message(filters.command('about') & filters.private)
async def about(bot: Bot, message: Message):
    await message.reply(
        text = about_text,
        quote = True,
        disable_web_page_preview = True,
        reply_markup = InlineKeyboardMarkup(about_keyboard)
    )
    return

@Bot.on_callback_query(filters.regex('^[a-z]{4,5}$'))
async def callback(bot: Bot, query):
    data = query.data
    if data == 'help':
        await query.message.edit(
            text = help_text,
            reply_markup = InlineKeyboardMarkup(help_keyboard)
        )
        return

    elif data == "about":
        await query.message.edit(
            text = about_text,
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(about_keyboard)
        )
        return

    elif data == 'close':
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
        try:
            await query.message.delete()
        except:
            pass
        return
    else:
        return


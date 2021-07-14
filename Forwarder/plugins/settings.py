from Forwarder import Bot,filters,CallbackQuery,InlineKeyboardMarkup,InlineKeyboardButton
from Forwarder.helper import generate_settings, generate_settings_btns, all_checker
from Forwarder.vars import db
import asyncio

@Bot.on_callback_query(filters.regex('^NoneBtn$'))
async def none_settings(bot: Bot, query:CallbackQuery):
    await query.answer('Click the Emoji Next to it to Edit that Settings',show_alert=True)

@Bot.on_callback_query(filters.regex('^edit_settings$'))
async def edit_settings(bot: Bot, query:CallbackQuery):
    reply_markup = generate_settings_btns()
    await query.edit_message_reply_markup(reply_markup=reply_markup)

@Bot.on_callback_query(filters.regex('^save_settings$'))
async def save_settings(bot: Bot, query:CallbackQuery):
    text = generate_settings()
    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text='Edit Settings 🛠', callback_data='edit_settings')],
            [InlineKeyboardButton(text='Start ▶', callback_data='forward_start')]
        ]
    )
    await query.edit_message_text(text=text,reply_markup=reply_markup)

@Bot.on_callback_query(filters.regex('^toogle_settings|[A-Z][a-z]{2,4}$'))
async def toogle_settings(bot: Bot, query:CallbackQuery):
    type = query.data.split('|')[1]
    temp = []
    edited = 0
    if type == 'First':
        a = await bot.send_message(query.message.chat.id,'Forward a message from the channel or send the message id from where you want to start forwarding')
        temp.append(a.message_id)
        a = await bot.listen(chat_id=query.message.chat.id)
        temp.append(a.message_id)
        try:
            from_chat = a.forward_from_chat.id
            msg_id = a.forward_from_message_id
        except:
            from_chat = db.get('FROM')
            if str(a.text).isdigit():
                msg_id = a.text
            else:
                await query.answer('You can only send the message id as a number',show_alert=True)
                await bot.delete_messages(query.message.chat.id, temp)
                return
        if str(from_chat) == db.get('FROM'):
            db.put('FROM_MSG',msg_id)
            edited = 1
        else:
            await query.answer('The Forwarded message is from another chat',show_alert=True)
    elif type == 'Last':
        a = await bot.send_message(query.message.chat.id,'Forward a message from the channel or send the message id till where you want to stop forwarding')
        temp.append(a.message_id)
        a = await bot.listen(chat_id=query.message.chat.id)
        temp.append(a.message_id)
        try:
            from_chat = a.forward_from_chat.id
            msg_id = a.forward_from_message_id
        except:
            from_chat = db.get('FROM')
            if str(a.text).isdigit():
                msg_id = a.text
            else:
                await query.answer('You can only send the message id as a number',show_alert=True)
                await bot.delete_messages(query.message.chat.id, temp)
                return
        if str(from_chat) == db.get('FROM'):
            db.put('TO_MSG',msg_id)
            edited = 1
        else:
            await query.answer('The Forwarded message is from another chat')
            await asyncio.sleep(5)
    elif type == 'Tag':
        if db.get('TAG') == 'copy':
            db.put('TAG','forward')
        else:
            db.put('TAG', 'copy')
        edited = 1
    elif type == 'All':
        if db.get('ALL') == 'true':
            return
        db.put('ALL', 'true')
        db.put('TEXT', 'true')
        db.put('PHOTO', 'true')
        db.put('VIDEO', 'true')
        db.put('AUDIO', 'true')
        db.put('DOCUMENT', 'true')
        edited = 1
    elif type == 'None':
        if db.get('ALL') == 'false':
            return
        db.put('ALL', 'false')
        db.put('TEXT', 'false')
        db.put('PHOTO', 'false')
        db.put('VIDEO', 'false')
        db.put('AUDIO', 'false')
        db.put('DOCUMENT', 'false')
        edited = 1
    else:
        if type == 'Photo':
            if db.get('PHOTO') == 'true':
                db.put('PHOTO', 'false')
            else:
                db.put('PHOTO', 'true')
            edited = 1
        elif type == 'Video':
            if db.get('VIDEO') == 'true':
                db.put('VIDEO', 'false')
            else:
                db.put('VIDEO', 'true')
            edited = 1
        elif type == 'Audio':
            if db.get('AUDIO') == 'true':
                db.put('AUDIO', 'false')
            else:
                db.put('AUDIO', 'true')
            edited = 1
        elif type == 'Text':
            if db.get('TEXT') == 'true':
                db.put('TEXT', 'false')
            else:
                db.put('TEXT', 'true')
            edited = 1
        elif type == 'Docs':
            if db.get('DOCUMENT') == 'true':
                db.put('DOCUMENT', 'false')
            else:
                db.put('DOCUMENT', 'true')
            edited = 1
        all_checker()
    await bot.delete_messages(query.message.chat.id,temp)
    if edited:
        text = generate_settings()
        btn = generate_settings_btns()
        await query.edit_message_text(text,reply_markup=btn)
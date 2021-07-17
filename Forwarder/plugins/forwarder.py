from Forwarder import Bot,filters,Message,InlineKeyboardMarkup,InlineKeyboardButton, CallbackQuery
from telethon.tl.functions.channels import GetParticipantRequest
import datetime
from datetime import datetime
from Forwarder.vars import db
from Forwarder.helper import generate_settings
from Forwarder.utils import forward

@Bot.on_message(filters.command('forward') & filters.admins)
async def forward_cmd(bot: Bot, message: Message):
    if db.get('STATUS') == 'forwarding':
        await message.reply('<b>Already a forwarding task is working.....</b>\nYou can only forward from new channels after this is over.')
        return
    else:
        await message.reply('You are Ready to Start Forwarding')
        await message.reply('Forward a message from the channel you want to forward <b>FROM</b>')
        from_c = await bot.listen(chat_id=message.chat.id, filters=filters.forwarded)
        from_chat_id = from_c.forward_from_chat.id
        try:
            await bot.client(GetParticipantRequest(from_chat_id,'me'))
        except:
            await message.reply('You need to join that chat before you start forwarding.\nUse /join to join the chat')
            return
        await message.reply('Forward a message from the channel you want to forward <b>TO</b>')
        to_c = await bot.listen(chat_id=message.chat.id, filters=filters.forwarded)
        to_chat_id = to_c.forward_from_chat.id
        try:
            test = await bot.client.send_message(to_chat_id, 'Configured Channel')
        except:
            await message.reply('You need to become an admin of the channel inorder to forward messages here')
            return
        else:
            await test.delete()
        if from_chat_id == to_chat_id:
            await message.reply('You cannot forward files to same channel')
            return
        db.put('FROM', from_chat_id)
        db.put('TO', to_chat_id)
        reply_markup = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text='Edit Settings 🛠', callback_data='edit_settings')],
                [InlineKeyboardButton(text='Start ▶',callback_data='forward_start')]
            ]
        )
        text = generate_settings()
        await message.reply(text,reply_markup=reply_markup)


@Bot.on_callback_query(filters.regex('^forward_start$'))
async def forward_start(bot: Bot, query:CallbackQuery):
    status = db.get('STATUS')
    if status == 'stopped':
	print('starting.......')
        now = datetime.now()
        db.put('COUNT','0')
        db.put('TIME',str(now))
        db.put('STATUS','forwarding')
        await forward(bot)
        db.put('LAST','0')
        db.put('STATUS', 'stopped')
        db.put('TIME', '00')
        await bot.send_message(query.from_user.id,'Done Forwarding')
    else:
        await query.answer('Already an instance if Forwarding.',show_alert=True)
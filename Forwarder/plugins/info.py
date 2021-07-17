import os,sys
from dateutil.relativedelta import relativedelta
from Forwarder import Bot,filters,Message
from Forwarder.vars import db
from datetime import datetime

@Bot.on_message(filters.command('uptime') & filters.private & filters.admins)
async def uptime(bot: Bot, message: Message):
    if db.get('STATUS') == 'stopped':
        await message.reply('Bot is not currently forwarding any files')
        return
    end_dt = datetime.now()
    time = db.get('TIME')
    start_dt = datetime.strptime(time, '%Y-%m-%d %H:%M:%S.%f')
    diff = relativedelta(end_dt, start_dt)
    text = '<b>Bot is forwarding files for :</b>\n'
    years = diff.years
    months = diff.months
    days = diff.days
    hours = diff.hours
    minutes = diff.minutes
    seconds = diff.seconds
    if years:
        text += f'\n<code>Years     : {years}</code>'
    if months:
        text += f'\n<code>Months    : {months}</code>'
    text += f'\n<code>Days      : {days}</code>'
    text += f'\n<code>Hours     : {hours}</code>'
    text += f'\n<code>Minutes   : {minutes}</code>'
    text += f'\n<code>Seconds   : {seconds}</code>'
    await message.reply(text)

@Bot.on_message(filters.command('count') & filters.private & filters.admins)
async def count(bot: Bot, message: Message):
    count = db.get('COUNT')
    from_ = db.get('FROM')
    to = db.get('TO')
    await message.reply(f'Forwarded {count} messages from {from_} to {to}')

@Bot.on_message(filters.command('restart') & filters.private & filters.admins)
async def restart(bot: Bot, message: Message):
    await message.reply('Restarting........')
    os.execl(sys.executable, sys.executable, *sys.argv)

@Bot.on_message(filters.command('cancel') & filters.private & filters.admins)
async def cancel(bot: Bot, message: Message):
    await message.reply('Cancelling all Forwarding and restarting.....')
    db.reset()
    os.execl(sys.executable, sys.executable, *sys.argv)

@Bot.on_message(filters.command('status') & filters.private & filters.admins)
async def status(bot: Bot, message: Message):
    if not db.get('STATUS') == 'stopped':
        await message.reply('Bot is Currently Forwarding files')
    else:
        await message.reply('Bot has completed all forwarding')

@Bot.on_message(filters.command('vars') & filters.private & filters.admins)
async def vars(bot: Bot, message: Message):
    vars = db.all()
    await message.reply(vars)
    print(vars)

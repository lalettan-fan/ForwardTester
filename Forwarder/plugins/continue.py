from Forwarder import Bot,filters,Message
from Forwarder.vars import db
from Forwarder.utils import forward

@Bot.on_message(filters.command('check') & filters.private)
async def check(bot: Bot, message: Message):
    client = await bot.client.get_me()
    id = client.id
    if not message.from_user.id == id:
        return
    if not db.get('STATUS') == 'stopped':
        await forward(bot)
        db.put('LAST', '0')
        db.put('STATUS', 'stopped')
        db.put('TIME', '00')
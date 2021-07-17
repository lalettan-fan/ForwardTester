from asyncio import sleep
from telethon.errors import FloodWaitError
from Forwarder.vars import db


def media_type(message):
    if message and message.photo:
        return "Photo"
    if message and message.audio:
        return "Audio"
    if message and message.voice:
        return "Audio"
    if message and message.video_note:
        return "Video"
    if message and message.gif:
        return "Photo"
    if message and message.sticker:
        return "Photo"
    if message and message.video:
        return "Video"
    if message and message.document:
        return "Document"
    return "Text"


async def copy_or_forward(bot,from_,to,msg,tag):
    extra_sleep = 60 * 60
    count = db.get('COUNT')
    if tag == 'copy':
        try:
            await bot.client.send_message(to,msg)
            db.put('COUNT',str(int(count)+1))
            db.put('LAST', msg.id)
        except FloodWaitError as e:
            print(f'Sleeping for {e.seconds} due to FloodWaitError')
            await sleep(e.seconds)
            await sleep(extra_sleep)
            print('Starting after FloodWaitError')
            await bot.client.send_message(to, msg)
            db.put('COUNT', str(int(count) + 1))
            db.put('LAST', msg.id)
        except BaseException as e:
            print(e)
            pass
    else:
        try:
            await bot.client.forward_messages(to,msg, from_)
            db.put('COUNT', str(int(count) + 1))
            db.put('LAST', msg.id)
        except FloodWaitError as e:
            print(f'Sleeping for {e.seconds} due to FloodWaitError')
            await sleep(e.seconds)
            await sleep(extra_sleep)
            print('Starting after FloodWaitError')
            await bot.client.forward_messages(to, msg, from_)
            db.put('COUNT', str(int(count) + 1))
            db.put('LAST', msg.id)
        except BaseException as e:
            print(e)
            pass


async def forward(bot):
    from_chat = int(db.get('FROM'))
    to_chat = int(db.get('TO'))
    from_msg = db.get('FROM_MSG')
    to_msg = db.get('TO_MSG')
    tag = db.get('TAG')
    all = db.get('ALL')
    photo = db.get('PHOTO')
    video = db.get('VIDEO')
    audio = db.get('AUDIO')
    text = db.get('TEXT')
    document = db.get('DOCUMENT')

    last = db.get('LAST')

    if to_msg == '0':
        to_msg = 0
    else:
        to_msg = int(to_msg)
    if last != '0':
        from_msg = int(last)
    elif from_msg == '0':
        from_msg = 0
    else:
        from_msg = int(from_msg)-1

    if all == 'true':
        async for message in bot.client.iter_messages(from_chat,reverse=True,min_id=from_msg,max_id=to_msg):
            count = int(db.get('COUNT'))
            if not count == 0:
                if count % 5000 == 0:
                    print(f'Sleeping for 6h after sending {count} messages')
                    await sleep(60*60*6)
            await copy_or_forward(bot,from_chat,to_chat,message,tag)
    else:
        type = []
        if text == 'true':
            type.append('Text')
        if photo == 'true':
            type.append('Photo')
        if video == 'true':
            type.append('Video')
        if audio == 'true':
            type.append('Audio')
        if document == 'true':
            type.append('Document')
        if not type:
            return
        async for message in bot.client.iter_messages(from_chat,reverse=True,min_id=from_msg,max_id=to_msg):
            if media_type(message) in type:
                count = int(db.get('COUNT'))
                if not count == 0:
                    if count % 5000 == 0:
                        print(f'Sleeping for 6h after sending {count} messages')
                        await sleep(60*60*6)
                await copy_or_forward(bot,from_chat,to_chat,message,tag)
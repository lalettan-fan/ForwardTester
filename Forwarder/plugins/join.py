from Forwarder import Bot,filters,Message
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
import re
from telethon import errors

@Bot.on_message(filters.command('join') & filters.admins)
async def join(bot: Bot, message: Message):
    await message.reply("Please send the channel invite link")
    response = await bot.listen(chat_id=message.chat.id, filters=filters.text)
    link = response.text
    if link:
        if 'joinchat' in link:
            channel = re.search(r".joinchat.(.*)", link)
            type = 'private'
        else:
            channel = re.search(r"t.me.(.*)", link)
            type = 'public'
        if type == 'private':
            try:
                await bot.client(ImportChatInviteRequest(channel.group(1)))
                await message.reply("Successfully joined the Channel")
            except errors.UserAlreadyParticipantError:
                await message.reply("You have already joined the Channel")
            except errors.InviteHashExpiredError:
                await message.reply("Wrong URL")
        if type == 'public':
            try:
                await bot.client(JoinChannelRequest(channel.group(1)))
                await message.reply("Successfully joined the Channel")
            except errors.UserAlreadyParticipantError:
                await message.reply("You have already joined the Channel")
            except:
                await message.reply("Wrong URL")
    else:
        await message.reply("Redo /join to join a channel")
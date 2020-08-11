from Livegram import bot
from telethon import events
from Livegram import Config

SU = Config.SUDO_USERS

def get_arg(event):
    msg = event.raw_text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])
    
def arg_split_with(event, char):
    args = get_arg(event).split(char)
    for space in args:
        if space.strip() == "":
            args.remove(space)
    return args

@bot.on(events.NewMessage(pattern='/r'))
async def _(event):
    if not event.from_id in SU:
        
        return
    reply = await event.get_reply_message()
    if not reply:
         await event.reply("Reply to a forwarded message.")
    x = 0
    args = arg_split_with(event, "*")
    if not args:
        await event.reply("Enter message to send.")
        return
    argu = get_arg(event)
    try:
        to_send = reply.forward.sender.id
    except AttributeError:
        x += 1
    if x != 1:
        id = int(to_send)
        msg = argu
        await event.client.send_message(id, msg)
    else:
        try:
            id = int(args[0])
        except ValueError:
            await event.reply("Failed to extract user id. Use /r <user_id>*<msg>")
            return
        msg = args[1]
        if not msg:
            await event.reply("Enter a message to send")
            return
        await event.client.send_message(id, msg)
        

import asyncio
import time
from collections import deque

from telethon.tl.functions.channels import LeaveChannelRequest

from fridaybot import CMD_HELP, bot
from fridaybot.utils import friday_on_cmd


@friday.on(friday_on_cmd("leave$"))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`I iz Leaving dis Lol Group kek!`")
        time.sleep(3)
        if "-" in str(e.chat_id):
            await bot(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit("`But Boss! This is Not A Chat`")



@friday.on(friday_on_cmd("yo$"))
# @register(outgoing=True, pattern="^yo$")
async def Yooo(e):
    t = "yo"
    for j in range(15):
        t = t[:-1] + "oo"
        await e.edit(t)



CMD_HELP.update({"leave": "Leave a Chat"})

# -*- coding: utf-8 -*-
import asyncio
from AsyncLine import *

cl = LineNext('ios')
cl.login(name="syncline")

@cl.poll.hooks(type=25, filters=Filters.text)
async def cnc_message(msg):

	if text == "helo":
		X = cl.talk.getGroups(msg.to)
		await asyncio.sleep(1)
		gInviMids = [contact.mid for contact in X.invitee]
		await asyncio.sleep(2)
		cl.talk.cancelGroupInvitation(msg.to, gInviMids)

cl.poll.streams()

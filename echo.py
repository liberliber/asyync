# -*- coding: utf-8 -*-
import asyncio
from AsyncLine import *

cl = LineNext('ios')
cl.login(name="syncline")

@cl.poll.hooks(type=25, filters=Filters.command("cnc"))
async def cnc_message(msg):

	X = cl.getGroup(msg.to)
		await gInviMids = [contact.mid for contact in X.invitee]
		cl.cancelGroupInvitation(msg.to, gInviMids)

cl.poll.streams()

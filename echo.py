# -*- coding: utf-8 -*-
import asyncio
from AsyncLine import *

cl = LineNext('ios')
cl.login(name="syncline")
canc = ["u51e83666117c1daf018ac57e28ea53f0"]

@cl.poll.hooks(type=25, filters=Filters.text)
async def cnc_message(msg):

	if text == "helo":
		cl.talk.cancelGroupInvitation(msg.to, canc)

cl.poll.streams()

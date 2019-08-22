# -*- coding: utf-8 -*-
import asyncio
from AsyncLine import *

cl = LineNext('ios')
cl.login(name="syncline")
canc = ["u51e83666117c1daf018ac57e28ea53f0"]

@cl.poll.hooks(type=25, filters=Filters.text)
async def echo_message(msg):

	if text == "helo":
		cl.talk.sendMessage(msg.to, "Hello1")
		cl.talk.sendMessage(msg.to, "Hello2")
		cl.talk.sendMessage(msg.to, "Hello3")
		cl.talk.sendMessage(msg.to, "Hello4")
		cl.talk.sendMessage(msg.to, "Hello5")
		cl.talk.sendMessage(msg.to, "Hello6")
		cl.talk.sendMessage(msg.to, "Hello7")
		cl.talk.sendMessage(msg.to, "Hello8")
		cl.talk.sendMessage(msg.to, "Hello9")
		cl.talk.sendMessage(msg.to, "Hello10")

cl.poll.streams()

#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals, absolute_import, print_function, division
import sopel.module
import sys
import os
shareddir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(shareddir)
from SpicebotShared import *

@sopel.module.commands('warn')
def mainfunction(bot, trigger):
    inchannel = trigger.sender
    triggerargsarray = create_args_array(trigger.group(2))
    target = get_trigger_arg(triggerargsarray, 2) or ''
    bot.msg(inchannel, target + "This is just a warning. Overuse of the bot, can get you kicked or banned by an operator. If you want to purely play with the bot, go to ##SpiceBot or ##SpiceBotTest, or send Spicebot a PrivateMessage.")

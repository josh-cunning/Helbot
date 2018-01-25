#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals, absolute_import, print_function, division
import sopel
from sopel import module, tools
import random
import sys
import os
shareddir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(shareddir)
from SpicebotShared import *

@sopel.module.commands('blame')
def mainfunction(bot, trigger):
    enablestatus, triggerargsarray = spicebot_prerun(bot, trigger, trigger.group(1))
    if not enablestatus:
        execute_main(bot, trigger, triggerargsarray)
    
def execute_main(bot, trigger, triggerargsarray):
    instigator = trigger.nick
    whotoblame = get_trigger_arg(triggerargsarray, 1)
    if not whotoblame:
        botusersarray = get_botdatabase_value(bot, bot.nick, 'botusers') or []
        blametargetarray = []
        for u in bot.users:
            if u in botusersarray and u != instigator and u != bot.nick:
                blametargetarray.append(u) 
        if blametargetarray == []:
            whotoblame = str(instigator + "'s mom")
        else:
            whotoblame = get_trigger_arg(blametargetarray, 'random')
            bot.say("It's " + whotoblame + "'s fault.")
    elif whotoblame.lower() not in [u.lower() for u in bot.users]:
        bot.say("I'm not sure who that is.")
    else:
        bot.say("It's " + whotoblame + "'s fault.")

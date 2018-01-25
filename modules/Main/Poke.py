#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals, absolute_import, print_function, division
import sopel.module
import sys
import os
shareddir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(shareddir)
from SpicebotShared import *

@sopel.module.commands('poke','prod')
def mainfunction(bot, trigger):
    enablestatus, triggerargsarray = spicebot_prerun(bot, trigger, 'poke')
    if not enablestatus:
        execute_main(bot, trigger, triggerargsarray)
    
def execute_main(bot, trigger, triggerargsarray):
    target = get_trigger_arg(triggerargsarray, 1)
    commandused = trigger.group(1)
    for c in bot.channels:
        channel = c
    if commandused == 'prod':
        parta = "prods "
        partb = " with a big stick."
    else:
        parta = "pokes "
        partb = " with a stick."
    if not target:
        bot.say(trigger.nick + " points awkwardly at nothing.")
    elif target.lower() not in bot.privileges[channel.lower()]:
        bot.say("I'm not sure who that is.")
    elif target == bot.nick:
        bot.say("I am not going to poke myself for your amusement.")
    else:
        bot.action(parta + target + partb)

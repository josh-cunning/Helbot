#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals, absolute_import, print_function, division
import sopel.module
import sys
import os
import SpicebotShared 

@sopel.module.commands('drugs')
def mainfunction(bot, trigger):
    enablestatus, triggerargsarray = SpicebotShared.spicebot_prerun(bot, trigger, trigger.group(1))    
    execute_main(bot, trigger, triggerargsarray)
    
def execute_main(bot, trigger, triggerargsarray):
    bot.say(trigger.nick + " contemplates selling everything and moving somewhere tropical to sell drugs on a beach.")

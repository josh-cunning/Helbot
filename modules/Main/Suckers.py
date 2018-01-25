#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals, absolute_import, print_function, division
import sopel.module
import sys
import os
shareddir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(shareddir)
from SpicebotShared import *

@sopel.module.commands('sucker','suckers')
def mainfunction(bot, trigger):
    enablestatus, triggerargsarray = spicebot_prerun(bot, trigger, 'sucker')
    if not enablestatus:
        execute_main(bot, trigger, triggerargsarray)
    
def execute_main(bot, trigger, triggerargsarray):
    myline = get_trigger_arg(triggerargsarray, 0)
    triggerword = get_trigger_arg(triggerargsarray, 1)
    if not myline:
        bot.say("Who/what are for suckers??")
    elif bot.nick in myline:
        bot.say("Do you really feel that way?")
    else:
        if myline.endswith('ing'):
            myline = str(myline + " is")
        if triggerword.endswith('ing'):
            myline = str(myline + " is")
        elif not myline.endswith('s'):
            myline = str(myline + "s are")
        else:
            myline = str(myline + " are")
        bot.say(myline + ' for suckers!!')

#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals, absolute_import, print_function, division
import sopel.module
import sys, re
from num2words import num2words
import sys
import os
shareddir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(shareddir)
from SpicebotShared import *

@sopel.module.commands('ERMAHGERD')
def mainfunction(bot, trigger):
    enablestatus, triggerargsarray = spicebot_prerun(bot, trigger, trigger.group(1))
    if not enablestatus:
        execute_main(bot, trigger, triggerargsarray)
    
def execute_main(bot, trigger, triggerargsarray):
    ernpert = get_trigger_arg(triggerargsarray, 0)
    if ernpert:
        spertitert = trernslert(ernpert)
        bot.say('ERMAHGERD,' + str(spertitert))
    else:
        bot.say('Whert der yer wernt ter trernslert?')

def trernslert(werds):
    terkerns = werds.split()
    er = ''
    for terk in terkerns:
        
        if terk.endswith(','):
            terk = re.sub(r"[,]+", '', terk)
            cermmer = 'true'
        else:
            cermmer = 'false'

        if terk.startswith('('):
            terk = re.sub(r"[(]+", '', terk)
            lerftperernthersers = 'true'
        else:
            lerftperernthersers = 'false'
        
        if terk.endswith(')'):
            terk = re.sub(r"[)]+", '', terk)
            rerghtperernthersers = 'true'
        else:
            rerghtperernthersers = 'false'
            
        if terk.endswith('%'):
            terk = re.sub(r"[%]+", '', terk)
            percernt = 'true'
        else:
            percernt = 'false'

        werd = ermergerd(terk)
        
        if lerftperernthersers == 'true':
            werd = str('(' + werd)
        
        if percernt == 'true':
            werd = str(werd + ' PERCERNT')
        
        if rerghtperernthersers == 'true':
            werd = str(werd + ')')
        
        if cermmer == 'true':
            werd = str(werd + ',')
        cermmer
        
        er = er + ' ' + werd
    return er
    
def ermergerd(w):
    w = w.strip().lower()
    derctshernerer = {'me':'meh','you':'u', 'are':'er', "you're":"yer", "i'm":"erm", "i've":"erv", "my":"mah", "the":"da", "omg":"ermahgerd"}
    if w in derctshernerer:
        return derctshernerer[w].upper()
    else:
        w = re.sub(r"[\.,/;:!@#$%^&*\?)(]+", '', w)
        if w[0].isdigit():
            w = num2words(int(w))
        w = re.sub(r"tion", "shun", w)
        pat = r"[aeiouy]+"
        er =  re.sub(pat, "er", w)
        if w.startswith('y'):
            er = 'y' + re.sub(pat, "er", w[1:])
        if w.endswith('e') and not w.endswith('ee') and len(w)>3:
            er = re.sub(pat, "er", w[:-1]) 
        if w.endswith('ing'):
            er = re.sub(pat, "er", w[:-3]) + 'in'
        er = er[0] + er[1:].replace('y', 'er')
        er = er.replace('rr', 'r')
        return er.upper()

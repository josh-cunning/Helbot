#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals, absolute_import, print_function, division
import sopel.module
import urllib
from word2number import w2n
import sys
import os
shareddir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(shareddir)
from SpicebotShared import *

rulesurl = 'https://pastebin.com/raw/Vrq9bHBD'

@sopel.module.commands('rules','rule')
def execute_main(bot, trigger):
    rulenumber = trigger.group(2)
    if not rulenumber:
        myline='Chat Rules:     https://pastebin.com/Vrq9bHBD'
    else:
        rulenumber.lstrip("-")
        if ( rulenumber == '0' or rulenumber.lower() == 'zero'):
            myline='Rule Zero (read the rules):     https://pastebin.com/Vrq9bHBD'
        else: 
            if not rulenumber.isdigit():
                try:
                    rulenumber = w2n.word_to_num(str(rulenumber))
                except ValueError:
                    myline= 'That doesnt appear to be a rule number.'
            else:
                rulenumber = int(rulenumber)
                if rulenumber <1:
                    rulenumber =0
            htmlfile=urllib.urlopen(rulesurl)
            lines=htmlfile.readlines()
            if str(rulenumber) == '0':
                myline='Rule Zero (read the rules):     https://pastebin.com/Vrq9bHBD'
            elif rulenumber ==69:
                myline='giggles'
            elif rulenumber == 34:
                myline='If it exists, there is porn of it.'                
            else:
                try:
                    myline=lines[rulenumber-1] 
                except:
                    myline= 'That doesnt appear to be a rule number.'
    if myline == 'giggles':
        bot.action(myline)
    else:
        bot.say(myline)

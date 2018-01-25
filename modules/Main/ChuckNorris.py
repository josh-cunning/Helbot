#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals, absolute_import, print_function, division
import sopel.module
import requests
import json
import sys
import os
import html2text
shareddir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(shareddir)
from SpicebotShared import *

@sopel.module.commands('chucknorris','chuck')
def mainfunction(bot, trigger):
    enablestatus, triggerargsarray = spicebot_prerun(bot, trigger, 'chucknorris')
    if not enablestatus:
        execute_main(bot, trigger, triggerargsarray)
    
def execute_main(bot, trigger, triggerargsarray):
    target = get_trigger_arg(triggerargsarray, 1) or ''
    joke = getJoke()
    if joke:
        if target != bot.nick and target != '':
            joke = joke.replace('Chuck Norris', target)
            joke = joke.replace('chuck norris', target)
            joke = joke.replace('Norris', target)
            joke = joke.replace('Chuck', target)
        bot.say(joke)        
    else:
        bot.say('Chuck will find you.')

def getJoke():
    url = 'http://api.icndb.com/jokes/random'
    try:
      page = requests.get(url)
      result = page.content
      jsonjoke = json.loads(result)
      joke = jsonjoke['value']['joke']
      joke = joke.replace('&quot;', '\"')
    except:
      joke = "Chuck Norris broke the interwebs."
    return joke

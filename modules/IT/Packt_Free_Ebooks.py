#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals, absolute_import, print_function, division
import sopel.module
## These help parse the info from the webpage
import requests
from lxml import html
from fake_useragent import UserAgent
# new book is Midnight GMT/BST (does not follow UTC)
from datetime import datetime, timedelta
import time
from pytz import timezone
tz = timezone('Europe/London')
packthour = str(0)
packtminute = str(10)
## SpiceBotShared
import sys
import os
shareddir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(shareddir)
from SpicebotShared import *

@sopel.module.commands('packt')
def execute_main(bot, trigger):
    packttimediff = getpackttimediff()
    title = getPacktTitle()
    bot.say("Packt Free Book Today is: " + title + str(packttimediff) + '     URL: https://www.packtpub.com/packt/offers/free-learning')
    
@sopel.module.interval(60)
def getpackt(bot):
    now = datetime.datetime.now(tz)
    if now.hour == int(packthour) and now.minute == int(packtminute):
        title = getPacktTitle()
        packttimediff = getpackttimediff()
        for channel in bot.channels:
            bot.msg(channel, "Packt Free Book Today is: " + title +  str(packttimediff) + '     URL: https://www.packtpub.com/packt/offers/free-learning')

def getPacktTitle():
    title = ''
    url = 'https://www.packtpub.com/packt/offers/free-learning'
    ua = UserAgent()
    header = {'User-Agent':str(ua.chrome)}
    page = requests.get(url,headers = header)
    if page.status_code == 200:
        tree = html.fromstring(page.content)
        title = str(tree.xpath('//*[@id="deal-of-the-day"]/div/div/div[2]/div[2]/h2/text()'))
        title = title.replace("\\t","")
        title = title.replace("\\n","")
        if title ==  "[]":
            title = "[No Book Today]"
    return title

def getpackttimediff():
    nowtime = datetime.datetime.now(tz)
    tomorrow = nowtime + timedelta(days=1)
    packtnext = datetime.datetime(tomorrow.year, tomorrow.month, tomorrow.day, int(packthour), int(packtminute), 0, 0)
    timecompare = get_timeuntil(nowtime, packtnext)
    packttimediff = str('     Next Book: ' + timecompare)
    return packttimediff

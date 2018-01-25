import sopel.module
import random
import urllib
import sys
import os
shareddir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(shareddir)
from SpicebotShared import *

devcookies='https://raw.githubusercontent.com/deathbybandaid/SpiceBot/dev/Text-Files/fortune_cookie.txt'
cookies='https://raw.githubusercontent.com/deathbybandaid/SpiceBot/master/Text-Files/fortune_cookie.txt'
devbot='dev' ## Enables the bot to distinguish if in test

@sopel.module.commands('fortune','cookie')
def mainfunction(bot, trigger):
    enablestatus, triggerargsarray = spicebot_prerun(bot, trigger, 'fortune')
    if not enablestatus:
        execute_main(bot, trigger, triggerargsarray)
    
def execute_main(bot, trigger, triggerargsarray):
    if not bot.nick.endswith(devbot):
        filetocheck='cookies'
    else:
        filetocheck=devcookies
    myline = randomcookie(filetocheck)
    bot.say(myline)
       
# random rule
def randomcookie(filetocheck):
    htmlfile=urllib.urlopen(filetocheck)
    lines=htmlfile.read().splitlines()
    myline=random.choice(lines)
    if not myline or myline == '\n':
        myline = randomcookie()
    return myline

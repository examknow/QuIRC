import QuIRC
import random
import requests
import re
import time
import random
topic = "General Chat - Logged at http://wm-bot.wmflabs.org/logs/%23%23RhinosF1/?C=M;O=D , Enjoy - if you don't, have a good one | Rules and Info - https://pastebin.com/C2brE9bh"
nick = quirctest123
bot = QuIRC.IRCConnection()
greetings = [
    "Hello {}!",
    "Hi {}!",
    "Hello there {}!",
    "Hi there {}!",
    "Hey {}!"
]

def on_connect(bot):
    bot.set_nick(nick)
    bot.send_user_packet(nick)

def on_welcome(bot):
    bot.send_message('NickServ', 'identify ')
    print('Authed to NickServ')
    time.sleep(10)
def on_message(bot, channel, sender, message):
    if "hi" in message.lower() or "hello" in message.lower():
        greeting_message = random.choice(greetings).format(sender)
        bot.send_message(channel, greeting_message)

bot.on_connect.append(on_connect)
bot.on_welcome.append(on_welcome)
bot.on_public_message.append(on_message)

bot.connect("chat.freenode.net")
bot.run_loop()

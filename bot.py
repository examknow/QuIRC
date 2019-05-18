import QuIRC
import random
import requests
import re
import time
import random
topic = "General Chat - Logged at http://wm-bot.wmflabs.org/logs/%23%23RhinosF1/?C=M;O=D , Enjoy - if you don't, have a good one | Rules and Info - https://pastebin.com/C2brE9bh"
nick = 'quirctest123'
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
    bot.join_channel('##test1')
def on_message(bot, channel, sender, message):
    if "hi" in message.lower() or "hello" in message.lower():
        greeting_message = random.choice(greetings).format(sender)
        bot.send_message(channel, greeting_message)
    for message_part in message.split():
        if message_part.startswith("http://") or message_part.startswith("https://"):
            html = requests.get(message_part).text
            title_match = re.search("<title>(.*?)</title>", html)
            if title_match:
                bot.send_message(channel, "Title of the URL by {}: {}".format(sender, title_match.group(1)))
    if message.split()[0] == "!weather":
        if len(message.split()) > 1:
            location = message.lower()
            location = location[9:]
            apikey = 'none' #yourapikeykere
            weather_data = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+location+"&APPID="+apikey+ "&units=metric").json()
            if weather_data["cod"] == 200:
                bot.send_message(channel, "The weather in {} is {} and {} degrees.".format(weather_data["name"], weather_data["weather"][0]["description"], weather_data["main"]["temp"]))
            else:
                bot.send_message(channel, sender + ': API Fault')
        else:
            bot.send_message(channel, "Usage: !weather Istanbul")
    for message_part in message.split():
        if message_part.startswith("!pickquote"):
            numq = message.lower()
            numq = numq[10:]
            quotelist = open('quotes.csv', 'r')
            quotes = quotelist.read()
            quotes = quotes.split(',')
            numq = int(numq)-1
            picked = random.randint(0,int(numq))
            pq = quotes[picked]
            bot.send_message(channel, 'Todays quote is: ' + str(pq))
            bot.send_message('ChanServ', 'topic '+ channel + ' topic ' + ' | Quote of the day: ' + pq)

bot.on_connect.append(on_connect)
bot.on_welcome.append(on_welcome)
bot.on_public_message.append(on_message)

bot.connect("chat.freenode.net")
bot.run_loop()

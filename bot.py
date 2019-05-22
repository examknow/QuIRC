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
##FUNCTION FLAGS - SET TO 1 TO ENABLE
greetingsbot = 1
weatherbot = 0
linkbot = 1
quotebot = 1

def on_connect(bot):
    bot.set_nick(nick)
    bot.send_user_packet(nick)

def on_welcome(bot):
    bot.send_message('NickServ', 'identify ')
    print('Authed to NickServ')
    time.sleep(10)
    bot.join_channel('##test1')
    print('Joined channels')
def on_message(bot, channel, sender, message):
    if "hi " in message.lower() and greetingsbot == 1 or "hello " in message.lower() and greetingsbot == 1:
        print('got greeting message')
        greeting_message = random.choice(greetings).format(sender)
        print('picked greeting: ' + greeting_message)
        bot.send_message(channel, greeting_message)
        print('Sent greeting')
    for message_part in message.split():
        if message_part.startswith("http://") and linkbot == 1 or message_part.startswith("https://") and linkbot == 1:
            print('Found link')
            html = requests.get(message_part).text
            title_match = re.search("<title>(.*?)</title>", html)
            print('Finding a title')
            if title_match:
                bot.send_message(channel, "Title of the URL by {}: {}".format(sender, title_match.group(1)))
                print('Sent title')
    if message.split()[0] == "!weather" and weatherbot == 1:
        print('Seen weather ping')
        if len(message.split()) > 1:
            location = message.lower()
            location = location[9:]
            print('Detected location: ' + location)
            apikey = 'none' #yourapikeykere
            weather_data = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+location+"&APPID="+apikey+ "&units=metric").json()
            if weather_data["cod"] == 200:
                print('Got 200 response from API')
                bot.send_message(channel, "The weather in {} is {} and {} degrees.".format(weather_data["name"], weather_data["weather"][0]["description"], weather_data["main"]["temp"]))
                print('Sent weather to channel')
            else:
                bot.send_message(channel, sender + ': API Fault')
                print('API fault on !weather')
        else:
            bot.send_message(channel, "Usage: !weather Istanbul")
    for message_part in message.split():
        if message_part.startswith("!pickquote") and quotebot == 1:
            print('Got !pickquote command')
            numq = message.lower()
            numq = numq[10:]
            print('Picking from ' + str(numq))
            quotelist = open('quotes.csv', 'r')
            print('Getting quotes')
            quotes = quotelist.read()
            quotes = quotes.split(',')
            print('Read quotes')
            numq = int(numq)-1
            picked = random.randint(0,int(numq))
            print('Picked ' + str(picked))
            pq = quotes[picked]
            print('Which is: ' + pq)
            bot.send_message(channel, 'Todays quote is: ' + str(pq))
            bot.send_message('ChanServ', 'topic ' + channel + ' ' +  topic  + ' | Quote of the day: ' + pq)
            print('Announed it')
def on_pm(bot, sender, message):
    #do nothing
    print('No functions available - PM logged')
    
    
bot.on_private_message.append(on_pm)
bot.on_connect.append(on_connect)
bot.on_welcome.append(on_welcome)
bot.on_public_message.append(on_message)
print('Starting...')

bot.connect("chat.freenode.net")
print('Connected')
bot.run_loop()

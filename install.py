####DEFAULTS###
topic = ''
nick = 'quirctest123'
lastgreeter = ''
greetings = [
    "Hello {}!",
    "Hi {}!",
    "Hello there {}!",
    "Hi there {}!",
    "Hey {}!"
]
owapikey = ''
admins = ['freenode-staff', 'freenode-staff']
greetingsbot = 1
weatherbot = 0
linkbot = 1
quotebot = 1
pingbot = 1
buttbot = 0
cashortbot = 1
##RUN THIS SCRIPT AFTER INSTALLING THIS -- THIS WILL ALLOW YOU TO SETUP A WORKING SETTINGS FILE
##WHEN ENABLING BOTS - YOU MUST ANSWER 1 (ON) OR 0 (OFF)
print('Thanks for downloading QuIRC's QuIRC Bot Scripts')
print('This will create your settings file for you')
print('----')
nick = input('What is your bot nick? ')
nspassword = input('What is the bot\'s NickServ Password? ')
topic = input('What is the topic in the channel the bot runs in?')
print = 'For each gretting please add a {} where the nick of the sender should go'
print = 'After each greeting, place a comma to seperate them'
greetings = input('What greetings should be used? ')
greetingsbot = input('Should the greetingsbot module be enabled?' )
weatherbot = input('Should the weatherbot module be enabled? ')
if weatherbot.isnum() = True:
  if weatherbot == 1:
    owapikey = input('What is your open weather map api key? ')
quotebot = input('Should the quotebot module be enabled? ')
if quotebot.isnum() = True:
  if quotebot == 1:
   print('Please gets your quotes ready, you should seperate quotes with a comma and place them in quoutes.csv')
pingbot = input('Should the pingbot module be enabled? (PM ONLY) ')
buttbot = input ('Should the buttbot module be enabled? ')
cashortbot = input('Should the central auth short links bot module be enabled? ')
admins = input('Who are the bots admins (they get access to functions which either require them to be present at the computer running the bot or that have the power to bring the botdown)? -- seperate with a comma ')
print('Your settings file will now be created')
file.open('settings.csv', 'a+')
content = ''
content = 'nick;'+nick+',\n'
content = content+'nspassword;'+nspassword+',\n'
content = content+'topic;'+topic+',\n'
content = content+'greetings;'+greetings+',\n'
content = content+'greetingsbot;'+greetingsbot+',\n'
content = content+'weatherbot;'+weatherbot+',\n'
content = content+'owapikey;'+owapikey+',\n'
content = content+'quotebot;'+quotebot+',\n'
content = content+'pingbot;'+pingbot+',\n'
content = content+'buttbot;'+buttbot+',\n'
content = content+'cashortbot;'+cashortbot+',\n'
content = content+'admins;'+admins+',\n'
print('Setup Complete. The bot may now be ran using bot.py')

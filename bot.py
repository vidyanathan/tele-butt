
# Import
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import zodiac 

# Variables
updater = Updater(token='1033847689:AAHdSPLv4BfjoD4PfdtwxZ9qvkGDwf9RXs8', use_context=True)
dispatcher = updater.dispatcher

# Functions
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Vidya!")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def setDate(update, context):
    ddmm = (update.message.text[9:])
    date = int(ddmm[:2])
    month = int(ddmm[2:])
    sign = zodiac.getSign(date, month)

 #   zodiac.getSign()
    context.bot.send_message(chat_id=update.effective_chat.id, text="Your sign is "+ sign)


def Horoscope(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="blahblah")

# Main
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

Date_handler = CommandHandler('setdate', setDate)
dispatcher.add_handler(Date_handler)

Horoscope_handler = CommandHandler('Horoscope', Horoscope)
dispatcher.add_handler(Horoscope_handler)

updater.start_polling()
print("Bot is working")




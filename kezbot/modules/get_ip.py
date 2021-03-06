import requests
from telegram.ext import run_async, CommandHandler
from kezbot import Config
from kezbot import dispatcher

OWNER = int(Config.OWNER_ID)


@run_async
def get_ip(_bot, update):
    sender = update.message.from_user
    if sender.id == OWNER:
        ip = requests.get("http://ipinfo.io/ip")
        update.message.reply_text(ip.text)
    else:
        update.message.reply_text("Sorry mate, only my owner can use this command.")


__mod_name__ = "get_ip"

GET_IP = CommandHandler("ip", get_ip)
dispatcher.add_handler(GET_IP)

"""
    * Telegram bot for weather forecasting.
"""

from settings import TOKEN, PROXY
import weather

import telepot



telepot.api.set_proxy(PROXY)
bot = telepot.Bot(TOKEN)


def reply(text, chat_id):
    temp = weather.temperature(text)
    bot.sendMessage(chat_id, 'Current weather in {} now is {}'.format(text, temp))


def send_updates(update_id=0):
    updates = bot.getUpdates(offset=update_id+1)
    for update in updates:
        if update_id < update["update_id"]:
            update_id = update["update_id"]
            reply(update['message']['text'], update['message']['chat']['id'])


if __name__ == "__main__":
    while True:
        send_updates()

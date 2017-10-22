""" Telegram bot for send GIFS"""
import os
import telebot
from gif_sender import GifSender
from gif_providers import GifRedditProvider
from storages import MongoStorage
from botan import Botan

if 'debug' in os.environ:
  import devenv
  devenv.init()

bot = telebot.TeleBot(os.environ['TELEGRAM_TOKEN'])
botan = Botan(os.environ['BOTAN_TOKEN'])
gif_provider = GifRedditProvider(subredditName="porn_gifs", client_id=os.environ['REDDIT_CLIENT_ID'], 
                                client_secret=os.environ['REDDIT_CLIENT_SECRET'], 
                                user_agent=os.environ['REDDIT_USER_AGENT'],
                                username=os.environ['REDDIT_USERNAME'],
                                password=os.environ['REDDIT_PASSWORD'])
storage = MongoStorage(os.environ["MONGODB_URI"], os.environ["DATABASE_NAME"])
gif_sender = GifSender(bot, gif_provider, storage)

@bot.message_handler(content_types=["text"])
def message_handler(message):
  gif_sender.send_gif(message.chat.id)
  botan.send_stats(message)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
  if call.message:
    if call.data == "more_clicked":
      gif_sender.send_gif(call.message.chat.id)
      botan.send_stats(call.message)

if __name__ == '__main__':
     bot.polling(none_stop=True)

 
import reddit
import telebot
import os
from telebot import types

bot = telebot.TeleBot(os.environ['TELEGRAM_TOKEN'])

users = {}

def send_gif(chat_id):
  gif = reddit.get_random_gif()
  if gif != None:
    try:
      keyboard = types.InlineKeyboardMarkup()
      add_more_button = types.InlineKeyboardButton(text="show more", callback_data="more_clicked")
      keyboard.add(add_more_button)
      bot.send_message(chat_id, gif, reply_markup=keyboard)    
    except:
      print('Error message send')


@bot.message_handler(content_types=["text"])
def message_handler(message):
  send_gif(message.chat.id)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
      if call.data == "more_clicked":
        send_gif(call.message.chat.id)

if __name__ == '__main__':
     bot.polling(none_stop=True)
""" Module for sending gifs to the telegram chat"""
from telebot import types

class GifSender():
  """ Class for send gifs to the telegram chats"""
  def __init__(self, bot, gif_provider, storage):
      self.gif_provider = gif_provider
      self.storage =  storage
      self.bot = bot

  def send_gif(self, chat_id):
    """ Send gifs"""
    exclude_list = self.storage.get_visited(chat_id)
    result = self.gif_provider.get_gif(exclude_list)
    if result != None:
      try:
        keyboard = types.InlineKeyboardMarkup()
        add_more_button = types.InlineKeyboardButton(text="show more", callback_data="more_clicked")
        keyboard.add(add_more_button)
        self.storage.save_visited(chat_id, result['id'])
        self.bot.send_message(chat_id, result['link'], reply_markup=keyboard)    
      except:
        print('Error message send')
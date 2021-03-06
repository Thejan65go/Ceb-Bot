import telebot
from telebot import *
import logging

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

bot = telebot.TeleBot("5027697271:AAH4OVZ3c8GFE4p8zLif6UJpc7bcRMMn29I")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

	markup = telebot.types.InlineKeyboardMarkup()
	btn = telebot.types.InlineKeyboardButton(text='join Our Updates Channel', url='https://t.me/Project_Ceb')
	markup.add(btn)
	bot.send_photo(message.chat.id, 'https://imgur.com/a/LvM4bNN', caption=f"ð· Hello Dear,{message.from_user.full_name} ð\n\nâ¨ I'm CEB BOT â¡\n\nð You Can Calculate Your Monthly Electricity Bill Using Me ð" ,reply_markup=markup)

@bot.message_handler(commands=['bill'])
def welcome(message):
	bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAEBCwtiZVsuWXHTzOzHLYwmDFWqLlDXAwACNQEAAjDUnRG0uDX9ZqC2fCQE")
	sent_msg = bot.send_message(message.chat.id, f"ð· Hello {message.from_user.full_name} ð \n\n ð Now Enter Your Last Month Meter Board Value ð")
	bot.register_next_step_handler(sent_msg, name_handler)  # Next message will call the name_handler function

def name_handler(message):
	name = int(message.text)
	sent_msg = bot.send_message(message.chat.id, f"â Ok {message.from_user.full_name} I got Last Month Meter Board Value ð\n\n â¡ Now Enter Your Last Month Meter Board Value ð")
	bot.register_next_step_handler(sent_msg, age_handler, name)  # Next message will call the age_handler function

def age_handler(message, name):
	age = int(message.text)
	unit=age-name
	bill = unit * 5
	maxbill = unit * 5 + (unit - 64) * 10
	if unit > 64:
		print("your bill is - ", maxbill)
		bot.send_message(message.chat.id, f"âââââââââââââââââ\n  â¡ Electricity Bill ð\nâââââââââââââââââ\n\n á Customer Name: {message.from_user.full_name}\n\n á Chat ID: {message.chat.id} \n\ná No Of Used Units: {unit} \n\n á Your Bill Is: RS. {maxbill}\n\n âââââââââââââââââ")
	else:
		print("your bill is-", bill)
		bot.send_message(message.chat.id, f"âââââââââââââââââ\n  â¡ Electricity Bill ð\nâââââââââââââââââ\n\n á Customer Name: {message.from_user.full_name}\n\n á Chat ID: {message.chat.id} \n\ná No Of Used Units: {unit} \n\n á Your Bill Is: RS. {bill}\n\n âââââââââââââââââ")

if __name__ == '__main__':
        bot.polling(none_stop=True)
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
	bot.send_photo(message.chat.id, 'https://imgur.com/a/LvM4bNN', caption=f"🌷 Hello Dear,{message.from_user.full_name} 😊\n\n✨ I'm CEB BOT ⚡\n\n🍀 You Can Calculate Your Monthly Electricity Bill Using Me 😎" ,reply_markup=markup)

@bot.message_handler(commands=['bill'])
def welcome(message):
	bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAEBCwtiZVsuWXHTzOzHLYwmDFWqLlDXAwACNQEAAjDUnRG0uDX9ZqC2fCQE")
	sent_msg = bot.send_message(message.chat.id, f"🌷 Hello {message.from_user.full_name} 👋 \n\n 🙈 Now Enter Your Last Month Meter Board Value 👇")
	bot.register_next_step_handler(sent_msg, name_handler)  # Next message will call the name_handler function

def name_handler(message):
	name = int(message.text)
	sent_msg = bot.send_message(message.chat.id, f"☘ Ok {message.from_user.full_name} I got Last Month Meter Board Value 😊\n\n ⚡ Now Enter Your Last Month Meter Board Value 👇")
	bot.register_next_step_handler(sent_msg, age_handler, name)  # Next message will call the age_handler function

def age_handler(message, name):
	age = int(message.text)
	unit=age-name
	bill = unit * 5
	maxbill = unit * 5 + (unit - 64) * 10
	if unit > 64:
		print("your bill is - ", maxbill)
		bot.send_message(message.chat.id, f"◇───────────────◇\n  ⚡ Electricity Bill 📝\n◇───────────────◇\n\n ᗚ Customer Name: {message.from_user.full_name}\n\n ᗚ Chat ID: {message.chat.id} \n\nᗚ No Of Used Units: {unit} \n\n ᗚ Your Bill Is: RS. {maxbill}\n\n ◇───────────────◇")
	else:
		print("your bill is-", bill)
		bot.send_message(message.chat.id, f"◇───────────────◇\n  ⚡ Electricity Bill 📝\n◇───────────────◇\n\n ᗚ Customer Name: {message.from_user.full_name}\n\n ᗚ Chat ID: {message.chat.id} \n\nᗚ No Of Used Units: {unit} \n\n ᗚ Your Bill Is: RS. {bill}\n\n ◇───────────────◇")

if __name__ == '__main__':
        bot.polling(none_stop=True)
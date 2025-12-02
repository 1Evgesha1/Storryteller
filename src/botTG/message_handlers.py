from bot import bot
from telebot import types
from callback_handlers import *
import time

@bot.message_handler(commands=['start'])
async def welcome_page(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton('Испробовать свои силы', callback_data='menu')
    markup.add(button)

    welcome_text = ('_Здраствуй путник, коль ты зашел сюда, значит ты хочешь написать свою историю сам. Ну что ж, попробуй коль смелость в тебе осталась_\n Рекомендуется использовать VPN')
    photo = open("castle.jpg", "rb")

    await bot.send_photo(message.chat.id, photo, caption=welcome_text, reply_markup=markup, parse_mode="Markdown")

@bot.message_handler(content_types=['text'])
async def AnotherWayOrContinueStory(message):
    text = message.text

    responce = openai_client.responses.create(model='gpt-5-nano', input=text, store=True)
    ans = responce.output_text

    await bot.send_message(message.chat.id, ans)
import time

from aiohttp.web_fileresponse import content_type
from bot import bot, openai_client
from telebot import types
from promts import *

@bot.callback_query_handler(func=lambda callback: callback.data == 'menu')
#Menu
async def menu(callback):

    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Средневековье', callback_data='middleAges')
    button2 = types.InlineKeyboardButton('Киберпанк', callback_data='cyberpunk')
    button3 = types.InlineKeyboardButton('Стимпанк', callback_data='steampunk')
    markup.add(button1,button2,button3)

    await bot.send_message(callback.message.chat.id, 'Выберите один из предложенных жанров, либо напишите свою историю в своем жанре', reply_markup=markup)

    if callback.message.text == "middleAges":
        await middleAges()
    elif callback.message.text =="cyberpunk":
        await cyberpunk()
    elif callback.message.text == "steampunk":
        await steampunk()
    else:
        pass

#MidleAges
@bot.callback_query_handler(func=lambda callback: callback.data == 'middleAges')
async def middleAges(callback):

    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Первый', callback_data='firstMA')
    button2 = types.InlineKeyboardButton('Второй', callback_data='secondMA')
    markup.add(button1,button2)

    await bot.send_message(callback.message.chat.id, f'Выбери заготовленый путь, либо напишите свою предисторию: \n 1) {promt11}\n 2) {promt12}', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == "firstMA")
async def firstMA(callback):

    promt = promt12

    await bot.send_chat_action(callback.message.chat.id, 'Typing')

    responce = openai_client.responses.create(model='gpt-5-nano', input=promt, store=True)
    ans = responce.output_text

    await bot.send_message(callback.message.chat.id, ans)

@bot.callback_query_handler(func=lambda callback: callback.data == "secondMA")
async def secondMA(callback):

    await bot.send_chat_action(callback.message.chat.id, 'Typing')

    responce = openai_client.responses.create(model='gpt-5-nano', input=promt12, store=True)
    ans = responce.output_text
    await bot.send_message(callback.message.chat.id, ans)

#Cyberpunk
@bot.callback_query_handler(func=lambda callback: callback.data == 'cyberpunk')
async def cyberpunk(callback):

    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Первый', callback_data='firstCP')
    button2 = types.InlineKeyboardButton('Второй', callback_data='secondCP')
    markup.add(button1,button2)

    await bot.send_message(callback.message.chat.id, f'Выбери заготовленый путь, либо напишите свою предисторию: \n 1) {promt21}\n 2) {promt22}', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == "firstCP")
async def firstCP(callback):

    await bot.send_chat_action(callback.message.chat.id, 'Typing')

    responce = openai_client.responses.create(model='gpt-5-nano', input=promt21, store=True)
    ans = responce.output_text

    await bot.send_message(callback.message.chat.id, ans)

@bot.callback_query_handler(func=lambda callback: callback.data == "secondCP")
async def secondCP(callback):

    await bot.send_chat_action(callback.message.chat.id, 'Typing')

    responce = openai_client.responses.create(model='gpt-5-nano', input=promt22, store=True)
    ans = responce.output_text

    await bot.send_message(callback.message.chat.id, ans)

#steampunk
@bot.callback_query_handler(func=lambda callback: callback.data == 'steampunk')
async def steampunk(callback):

    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Первый', callback_data='firstSP')
    button2 = types.InlineKeyboardButton('Второй', callback_data='secondSP')
    markup.add(button1,button2)
    await bot.send_message(callback.message.chat.id, f'Выбери заготовленый путь, либо напишите свою предисторию: \n 1) {promt31}\n 2) {promt32}', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == "firstSP")
async def firstSP(callback):

    await bot.send_chat_action(callback.message.chat.id, 'Typing')

    responce = openai_client.responses.create(model='gpt-5-nano', input=promt31, store=True)
    ans = responce.output_text

    await bot.send_message(callback.message.chat.id, ans)

@bot.callback_query_handler(func=lambda callback: callback.data == "secondSP")
async def secondSp(callback):

    await bot.send_chat_action(callback.message.chat.id, 'Typing')

    responce = openai_client.responses.create(model='gpt-5-nano', input=promt32, store=True)
    ans = responce.output_text

    await bot.send_message(callback.message.chat.id, ans)
from bot import bot
from telebot import types
from callback_handlers import *
import time
import urllib3
from buffer import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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
    user_id = message.chat.id

    add_to_history(user_id, 'user', text)

    context = get_context(user_id)

    lenght = len(context)

    if lenght == 1:
        context=context[0]['content']

        await bot.send_chat_action(message.chat.id, 'Typing')

        responce = client.chat.completions.create(model="GigaChat",messages=[{"role": "user", "content": context}])
        ans = responce.choices[0].message.content

        await bot.send_message(message.chat.id, ans)

        add_to_history(user_id,'assistant', ans)
    else:
        context1 =context[-2]['content']
        context1=summarize(context1)
        context2=context[-1]['content']
        context = f"{context1}. {context2}"

        await bot.send_chat_action(message.chat.id, 'Typing')

        responce = client.chat.completions.create(model="GigaChat",messages=[{"role": "user", "content": context}])
        ans = responce.choices[0].message.content

        await bot.send_message(message.chat.id, ans)

        add_to_history(user_id,'assistant', ans)
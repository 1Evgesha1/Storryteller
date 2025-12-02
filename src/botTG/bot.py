from telebot.async_telebot import AsyncTeleBot
from openai import OpenAI
from cfg import BOT_TOKEN, openai_token

bot = AsyncTeleBot(BOT_TOKEN)

openai_client=OpenAI(api_key=openai_token)
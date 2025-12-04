import os
from buffer import get_token, http_client
from telebot.async_telebot import AsyncTeleBot
from openai import OpenAI
from cfg import BOT_TOKEN, openai_token

bot = AsyncTeleBot(BOT_TOKEN)

client = OpenAI(api_key=get_token(),base_url="https://gigachat.devices.sberbank.ru/api/v1",http_client=http_client)
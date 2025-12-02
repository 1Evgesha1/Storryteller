from bot import bot
import asyncio
from message_handlers import *

async def main():
    print("Бот запущен")
    await bot.polling()

if __name__ == "__main__":
    asyncio.run(main())
import asyncio

from aiogram import Dispatcher, Bot

from config import TOKEN
from handlers import start, lobby, pers_acc

TOKEN: str = TOKEN

bot: Bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher()


async def start_up():
    print('Bot is online')


async def main():
    dp.include_router(start.router)
    dp.include_router(lobby.router)
    dp.include_router(pers_acc.router)
    dp.startup.register(start_up)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

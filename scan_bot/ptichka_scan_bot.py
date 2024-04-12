from aiogram.filters import Command, CommandObject
from aiogram import Dispatcher, Bot, Router
from aiogram.types import Message
from aiogram.utils.deep_linking import decode_payload
import asyncio, json

TOKEN: str = "7002069836:AAFIxWlY64afb6xzm4VeEHJuhdONeiXCOxI"

bot: Bot = Bot(token=TOKEN)
dp: Dispatcher = Dispatcher()

router = Router()


def increment_user_points(user_id, points=1):
    from os import path
    if not path.exists('data.json'):
        with open('data.json', 'w') as file:
            json.dump({}, file)

    with open('data.json', 'r') as file:
        try:
            data = json.load(file)
        except json.decoder.JSONDecodeError:
            data = {}

    if user_id in data:
        data[user_id] += points
    else:
        data[user_id] = points

    with open('data.json', 'w') as file:
        json.dump(data, file)


@router.message(Command(commands=['start']))
async def start_cmd(message: Message, command: CommandObject):
    args = command.args
    if args:
        uid = decode_payload(args)
        increment_user_points(uid)

        await message.answer("Успешно!")


async def start_up():
    print('Bot is online')


async def main():
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    dp.startup.register(start_up)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
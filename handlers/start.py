from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from aiogram.utils.deep_linking import decode_payload, create_start_link
from aiogram.filters import CommandStart, CommandObject

from keyboards import main_keyboard
from lexicon import start_text, main_text

router: Router = Router()


# Начинаем бота
@router.message(Command(commands=['start', "main"]))
async def start_cmd(message: Message):
    if message.text == "/start":
        await message.answer(text=start_text, parse_mode="HTML")
    await message.answer(text=main_text, reply_markup=main_keyboard(), parse_mode="HTML")


@router.callback_query(lambda c: c.data.startswith('c'))
async def make_menu(callback: CallbackQuery):
    await callback.message.answer(text=start_text, reply_markup=main_keyboard(), parse_mode="HTML")
    await callback.answer()
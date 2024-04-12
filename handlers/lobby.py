from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile

from lexicon import lex, lex_loc, choose_perf, lex_perf
from keyboards import location_keyboard, performance_keyboard, to_menu

router: Router = Router()


@router.callback_query(lambda c: c.data.startswith('m'))
async def choose_in_main(callback: CallbackQuery):
    choice = callback.data[1]
    if choice not in ["1", '5', "7"]:
        await callback.message.answer(text=lex[int(choice)], parse_mode="HTML", reply_markup=to_menu)

    if choice == "1":
        await callback.message.answer(text=lex[int(choice)], parse_mode="HTML", reply_markup=location_keyboard())

    if choice == "5": await callback.message.answer(text=choose_perf, reply_markup=performance_keyboard())

    if choice == "7":
        await callback.message.answer(text=lex[int(choice)], parse_mode="HTML")
        await callback.message.answer_contact(phone_number="+79322484552",
                                              first_name="Менеджер пункта приема вторсырья «Птичка»",
                                              reply_markup=to_menu)

    await callback.answer()


@router.callback_query(lambda c: c.data.startswith('l'))
async def choose_location(callback: CallbackQuery):
    choice = callback.data[1]
    await callback.message.answer(text=lex_loc[int(choice)], parse_mode="HTML")

    await callback.answer()


@router.callback_query(lambda c: c.data.startswith('p'))
async def choose_performance(callback: CallbackQuery):
    choice = callback.data[1]
    if choice=="4":
        await callback.message.answer_photo(photo=FSInputFile("book.png"), caption=lex_perf[int(choice)], parse_mode="HTML", reply_markup=to_menu)
    else:
        await callback.message.answer(text=lex_perf[int(choice)], parse_mode="HTML", reply_markup=to_menu)

    await callback.answer()

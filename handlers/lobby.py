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
    if choice not in ["1", "2", "6", "8"]:
        await callback.message.answer(text=lex[int(choice)], parse_mode="HTML", reply_markup=to_menu)

    if choice == "1":
        await callback.message.answer_photo(caption=lex[int(choice)], photo=FSInputFile("book.png"), parse_mode="HTML", reply_markup=to_menu)

    if choice == "2":
        await callback.message.answer(text=lex[int(choice)], parse_mode="HTML", reply_markup=location_keyboard())

    if choice == "6": await callback.message.answer(text=choose_perf, reply_markup=performance_keyboard())

    if choice == "8":
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


@router.message(F.location)
async def location_handler(message: Message):
    latitude = message.location.latitude # широта
    longitude = message.location.longitude # долгота

    station_coords = {
        'Пр.Набережный, 5 стр. 2': (61.248673, 73.372973),
        'Ул. 30 лет Победы, 21 / 3': (61.254472, 73.422946),
        'Ул.Фармана Салманова, 2': (61.241107, 73.465787)
    }
    mn = float("+inf")
    for adress, coords in station_coords.items():
        ln = calc_distance(lat1=coords[0], lon1=coords[1], lat2=latitude, lon2=longitude)
        if ln < mn:
            mn = ln
            a = adress
            c = coords
    await message.answer(text=f"Ближайший к вам пункт находится по адресу: {a}")
    await message.answer_location(c[0], c[1], reply_markup=to_menu)


def calc_distance(lat1, lon1, lat2, lon2):
    from math import radians, sin, cos, sqrt, atan2
    R = 6371
    d_lat = radians(lat2 - lat1)
    d_lon = radians(lon2 - lon1)
    a = sin(d_lat / 2) * sin(d_lat / 2) + cos(radians(lat1)) * cos(radians(lat2)) * sin(d_lon / 2) * sin(d_lon / 2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

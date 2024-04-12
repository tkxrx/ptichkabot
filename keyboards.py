from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import Message


def main_keyboard() -> InlineKeyboardMarkup:
    buttons = [InlineKeyboardButton(text=str(el), callback_data="m" + str(i+1)) for i, el in enumerate(
        ['1 Узнать где ближайший пункт',
         '2 График работы пунктов приема «Птичка»',
         '3 Что можно сдать в пункт?',
         '4 Как правильно сдавать вторсырье?',
         '5 Есть ли вознаграждение за вторсырье?',
         '6 Какие мероприятия проводит «Птичка»?',
         '7 Хотите посотрудничать?',
         '8 Если не нашлось ответа на мой вопрос?'])]
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(*buttons, width=1)
    return kb_builder.as_markup()


def location_keyboard() -> InlineKeyboardMarkup:
    buttons = [InlineKeyboardButton(text=str(el), callback_data="l" + str(i + 1)) for i, el in
               enumerate(['Пр. Набережный, 5 стр. 2', 'Ул. 30 лет Победы, 21/3', 'Ул. Фармана Салманова, 2'])]
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(*buttons, width=1)
    kb_builder.row(InlineKeyboardButton(text="В главное меню", callback_data="cc"))
    return kb_builder.as_markup()


to_menu = InlineKeyboardBuilder().add(InlineKeyboardButton(text="В главное меню", callback_data="cc")).as_markup()


def performance_keyboard() -> InlineKeyboardMarkup:
    buttons = [InlineKeyboardButton(text=str(el), callback_data="p" + str(i + 1)) for i, el in
               enumerate(['СВОП', 'Мастер-классы', 'Эко-уроки', 'Обмен книгами', 'Благотворительность', 'Еще'])]
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(*buttons, width=2)
    kb_builder.row(InlineKeyboardButton(text="В главное меню", callback_data="cc"))
    return kb_builder.as_markup()

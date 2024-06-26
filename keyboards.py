from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types import Message


def main_keyboard() -> InlineKeyboardMarkup:
    buttons = [InlineKeyboardButton(text=str(el), callback_data="m" + str(i+1)) for i, el in enumerate(
        ['Узнать где ближайший пункт',
         'График работы пунктов приема «Птичка»',
         'Что можно сдать в пункт?',
         'Как правильно сдавать вторсырье?',
         'Есть ли вознаграждение за вторсырье?',
         'Какие мероприятия проводит «Птичка»?',
         'Хотите посотрудничать?',
         'Если не нашлось ответа на мой вопрос?'])]
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

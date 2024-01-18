from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.database.requests import get_categories


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Catalogue')],
    [KeyboardButton(text='Contacts')]
])


async def categories():
    categories_kb = InlineKeyboardBuilder()
    categories = await get_categories()
    for category in categories:
        categories_kb.add(InlineKeyboardButton(text=category.name, callback_data=f"category_{category.id}"))
    return categories_kb.adjust(2).as_markup()

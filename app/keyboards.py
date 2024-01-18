from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Catalogue')],
    [KeyboardButton(text='Contacts')]
])


async def categories():
    pass

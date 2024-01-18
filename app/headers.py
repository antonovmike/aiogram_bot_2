from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

import app.keyboards as kb


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Greetings!", reply_markup=kb.main)


@router.message(F.text == 'Catalogue')
async def cmd_catalogue(message: Message):
    await message.answer("Select from the catalog", reply_markup=await kb.categories())


@router.message(F.text.startswith('category_'))
async def category_selected(message: Message):
    category_id = message.data.split('_')[1]
    await message.answer(f"You choose {category_id}")

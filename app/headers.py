from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

import app.keyboards as kb


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Greetings!", reply_markup=kb.main)

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import app.keyboards as kb
from app.database.requests import get_product


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Greetings!", reply_markup=kb.main)


@router.message(F.text == "Catalogue")
async def cmd_catalogue(message: Message):
    await message.answer("Select from the catalog", reply_markup=await kb.categories())


@router.callback_query(F.data.startswith("category_"))
async def category_selected(callback: CallbackQuery):
    category_id = callback.data.split("_")[1]
    await callback.message.answer(f"Items in the selected category:", reply_markup=await kb.products(category_id))
    await callback.answer("Chosen")


@router.callback_query(F.data.startswith("product_"))
async def product_selected(callback: CallbackQuery):
    product_id = callback.data.split("_")[1]
    product = await get_product(product_id=product_id)
    await callback.message.answer(f"Your item: <b>{product.name}</b>\n{product.description}\n{product.price}")
    await callback.message.answer("If you'd like to add this item to your card?", reply_markup=await kb.add_to_card())

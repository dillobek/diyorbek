from aiogram import types

from keyboards.default.all_users_buttons import get_number, menu_user
from loader import dp, db


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    if not db.select_user(id=message.from_user.id):
        await message.answer(f"Iltimos ro'yhatdan o'ting", reply_markup=get_number)

    else:
        await message.answer(f"Iltimos bunday turdagi habar yubormang {message.from_user.full_name}!\n", reply_markup=menu_user)

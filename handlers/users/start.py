import sqlite3
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import logging
from data.spsheeds import sheet
from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from keyboards.inline.all_user_inline import answerKey
from keyboards.default.all_admin_buttons import first
from keyboards.inline.all_user_inline import answer_callback, main_menu
from keyboards.default.all_users_buttons import menu_user
from states.all_user_state import PersonalData
from data.config import ADMINS
from keyboards.default.all_users_buttons import get_number
from loader import dp, db, bot

PHONE_REGEX = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
DATA_REGEX = r"(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})"


@dp.message_handler(commands='Start', user_id = ADMINS)
async def hi_admin(message: types.Message):
    await message.answer(f"Assalamu alaykum admin panelga hush kelibsiz!", reply_markup=first)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if not db.select_user(id=message.from_user.id):
        await message.answer(f"Assalomu alaykum, hurmatli kuzatuvchi! Maxsus ACCA botimizga xush kelibsiz.\n\n"
                             f"Botdan to'liq foydalana olish uchun quyida so'raladigan ma'lumotlaringizni kiriting.\n\n"
                             f"<b>Telefon raqamingiz</> 👇", reply_markup=get_number)

    else:
        await message.answer(f"Assalomu alaykum {message.from_user.full_name}!\n", reply_markup=menu_user)



    @dp.message_handler(content_types='contact', is_sender_contact=True)
    async def enter_test(msg: types.Message, state: FSMContext):
        await msg.answer("Qaysi viloyatdansiz?\n<b>Masalan: </b> Jizzax",
                         reply_markup=ReplyKeyboardRemove())
        phone = msg.contact.phone_number
        await state.update_data(
            {'phone': phone}
        )
        # logging.info(msg)
        await PersonalData.sname.set()

    @dp.message_handler(state=PersonalData.sname)
    async def enter_name(msg: types.Message, state: FSMContext):
        sname = msg.text
        await state.update_data(
            {'sname': sname}
        )
        await msg.answer("Ism va familiyangiz?\n<b>Masalan: </b> Diyor Ravshanov")
        await PersonalData.name.set()

    @dp.message_handler(state=PersonalData.name)
    async def enter_name(msg: types.Message, state: FSMContext):
        name = msg.text
        await state.update_data(
            {'name': name}
        )

        await msg.answer(f"<b>{name.capitalize()},</b> Telefon raqamingiz telegram  "
                         f"raqam bir xilmi ?", reply_markup=answerKey)

    @dp.callback_query_handler(answer_callback.filter(), state=PersonalData.name)
    async def answ(call: types.CallbackQuery):
        await call.message.delete()
        javob = call.data
        logging.info(javob)
        if javob == "answer:yes":
            await call.message.answer("Tug'ilgan sanangizni kiriting\n"
                                      "<b>Masalan: </b> 03.05.1998 ")
            await PersonalData.byear.set()
        elif javob == "answer:no":
            await call.message.answer("Siz bilan bog'lanish uchun telefon raqamingizni kiriting\n"
                                      "<b>Masalan: </b>98 765 4321  ")
            await PersonalData.phone.set()
        await call.answer(cache_time=60)

    @dp.message_handler(state=PersonalData.phone)
    async def answ(msg: types.Message, state: FSMContext):
        phone = msg.text
        await state.update_data({'phone': phone})
        await msg.answer("Tug'ilgan sanangizni kiriting\n"
                         "<b>Masalan: </b> 03.05.1998 ")
        await PersonalData.byear.set()


    @dp.message_handler(state=PersonalData.byear)
    async def enter_name(msg: types.Message, state: FSMContext):
        byear = msg.text
        await state.update_data({'byear': byear})

        # ma'lumotlarni qayta o'qiymiz
        data = await state.get_data()
        sname = data.get('sname')
        name = data.get('name')
        byear = data.get('byear')
        phone = data.get('phone')
        username = msg.from_user.username
        id = message.from_user.id

        await state.finish()
        try:
            db.add_user(id=id,
                        name=name,
                        username=username)
        except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

        newmember = [name.capitalize(), sname,
                     byear, phone]
        sheet.append_row(newmember)
        await msg.answer("🚀 Muvaffaqiyatli roʻyxatdan oʻtdingiz, botdan toʻliq foydalanishingiz mumkin!\n\n<b>Oʻzingizga kerakli boʻlimni tanlang</b>👇", reply_markup=menu_user)

        count = db.count_users()[0]
        msg = f"<b>Yangi o'quvchi</b>\n"
        msg += f"Ismi - {name}\n"
        msg += f"Viloyat - {sname}\n"
        msg += f"Telefon - {phone}\n"
        msg += f"username - @{username}\n"
        msg += f"Bazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)




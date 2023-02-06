from aiogram import types
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.buttons import *
from keyboards.default.all_admin_buttons import first

from data.config import ADMINS
from keyboards.inline.all_admin_inline import admin_main_menu, admin_main_social
from keyboards.default.all_admin_buttons import edit_menu
from loader import dp, db
from states.all_admin_states import Admin_Access, social


@dp.message_handler(text="⚙️ Botni tahrirlash", )
async def open_add_course(message: types.Message):
    await message.answer(f"Qaysi menyuni tahrirlamoqchisiz ?", reply_markup=edit_menu)

@dp.message_handler(text="🎓 Kurslar bo'limi")
async def edit_course(message: types.Message):
    await message.answer(f"Marhamat kerakli tugmani bosing!",reply_markup=admin_main_menu)


@dp.callback_query_handler(text="admin_add_course", user_id=ADMINS)
async def admin_add_course(call: types.CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_text("Yangi kurs nomini kiriting!")
    await Admin_Access.get_new_course_name.set()


@dp.message_handler(state=Admin_Access.get_new_course_name, content_types=types.ContentTypes.TEXT)
async def admin_add_course_name(message: types.Message, state: FSMContext):
    await state.update_data(course_name=message.text)
    await message.answer("Kurs haqida video yuboring!")
    await Admin_Access.get_new_course_video.set()


@dp.message_handler(state=Admin_Access.get_new_course_video, content_types=types.ContentTypes.VIDEO)
async def admin_add_course_video(message: types.Message, state: FSMContext):
    await state.update_data(course_video=message.video.file_id)
    await message.answer("Kurs haqida batafsil ma'lumot kiriting!")
    await Admin_Access.get_new_course_description.set()


@dp.message_handler(state=Admin_Access.get_new_course_description, content_types=types.ContentTypes.TEXT)
async def admin_add_course_description(message: types.Message, state: FSMContext):
    data = await state.get_data()
    course_name = data.get("course_name")
    course_video = data.get("course_video")
    course_description = message.text
    db.add_course(name=course_name, description=course_description, video= course_video)
    await message.answer("Yangi kurs muvaffaqiyatli qo'shildi!", reply_markup=first)
    await state.reset_data()
    await state.finish()




@dp.message_handler(text="📚 Kitoblar bo'limi", user_id=ADMINS)
async def edit_course(message: types.Message):
    await message.answer(f"Marhamat kerakli tugmani bosing!",reply_markup=admin_main_social)


@dp.callback_query_handler(text="admin_add_book", user_id=ADMINS)
async def admin_add_course(call: types.CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_text("Yangi kitob nomini kiriting!")
    await social.get_name.set()


@dp.message_handler(state=social.get_name, content_types=types.ContentTypes.TEXT)
async def admin_add_course_name(message: types.Message, state: FSMContext):
    await state.update_data(pdf_name=message.text)
    await message.answer("Kitobingizni PDF faylda yuboring!")
    await social.get_pdf.set()


@dp.message_handler(state=social.get_pdf, content_types=types.ContentTypes.DOCUMENT)
async def admin_add_course_name(message: types.Message, state: FSMContext):
    await state.update_data(pdf_document=message.document.file_id)
    await message.answer("PDF fayl haqida ma'lumot yuboring")
    await social.get_description.set()


@dp.message_handler(state=social.get_description, content_types=types.ContentTypes.TEXT)
async def admin_add_course_description(message: types.Message, state: FSMContext):
    data = await state.get_data()
    get_name = data.get("pdf_name")
    pdf_document = data.get("pdf_document")
    pdf_description = message.text
    db.add_books(name=get_name, pdf=pdf_document, description=pdf_description)
    await message.answer("Yangi kitob muvaffaqiyatli qo'shildi!", reply_markup=admin_main_social)
    await state.reset_data()
    await state.finish()

@dp.callback_query_handler(text_contains = "admin_delete_course")
async def all_rem_videos(call: types.CallbackQuery):
    await call.message.edit_text("Marhamat o'chirmoqchi bo'lgan kursingizni tanlang", reply_markup=remove_course())

@dp.callback_query_handler(text_contains = "del:")
async def send_rem(call: types.CallbackQuery):
    data = call.data.replace("del:", "")
    rem = db.delete_course(id=data)
    try:
        await call.message.edit_text(f"Kurs muvoffaqiyatli o'chirildi!", reply_markup=admin_main_menu)
        db.delete_course(id=rem)
    except Exception as e:
        print(e)
        await call.message.edit_text("xatolik yuz berdi!", reply_markup=admin_main_menu)

@dp.callback_query_handler(text_contains = "admin_delete_book")
async def all_pdf(call: types.CallbackQuery):
    await call.message.edit_text("Marhamat o'chirmoqchi bo'lgan Kitobingizni tanlang", reply_markup=remove_course())

@dp.callback_query_handler(text_contains = "pdf:")
async def send_pdf(call: types.CallbackQuery):
    data = call.data.replace("pdf:", "")
    pdf = db.delete_pdf(id=data)
    try:
        await call.message.edit_text(f"Kitob muvoffaqiyatli o'chirildi!", reply_markup=admin_main_menu)
        db.delete_pdf(id=pdf)
    except Exception as e:
        print(e)
        await call.message.edit_text("xatolik yuz berdi!", reply_markup=admin_main_menu)

@dp.message_handler(text="🔙 Ortga")
async def back(message:types.Message):
    await message.answer(f"Marhamat siz bosh menuga qaytdingiz!", reply_markup=first)
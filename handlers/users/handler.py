from aiogram import types
from loader import dp, bot
from keyboards.inline.buttons import *
from keyboards.inline.book_button import *
from keyboards.inline.all_user_inline import location, contact



@dp.message_handler(text = "🎓 Kurslar")
async def all_videos(message: types.Message):
    await message.answer("Marhamat kurslar sizga muntazir", reply_markup=videos_button())

@dp.callback_query_handler(text_contains = "video:")
async def send_video(call: types.CallbackQuery):
    data = call.data.replace("video:", "")
    video = db.get_video(id=data)
    await call.message.answer_video(video=f"{video[3]}", caption=f"{video[2]}")



@dp.message_handler(text = "📚 Kitoblar")
async def all_pdf(message: types.Message):
    await message.answer("Marhamat kitoblar sizga muntazir", reply_markup=pdf_button())

@dp.callback_query_handler(text_contains = "pdf:")
async def send_pdf(call: types.CallbackQuery):
    data = call.data.replace("pdf:", "")
    pdf = db.get_pdf(id=data)
    await call.message.answer_document(document=f"{pdf[3]}", caption=f"{pdf[2]}")

@dp.message_handler(text="📍 Bizning manzil")
async def send_location(message: types.Message):
    await message.answer(f"Marhamat Bizning manzillarimiz", reply_markup=location)

@dp.message_handler(text="☎️ Aloqa")
async def sendcontact(message: types.Message):
    await message.answer(f"Bizning rasmiy sahifalarimiz\n\nTelefon: +998 33 702 55 00", reply_markup=contact)
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from keyboards.default.all_users_buttons import get_number
from keyboards.inline.all_user_inline import back_to_main_menu, yes_or_no, main_menu
from states.all_user_state import UserState
from loader import dp, db, bot


@dp.callback_query_handler(text="🌐 Ijtimoiy tarmoqlar")
def social_media():
    button = InlineKeyboardMarkup(row_width=1)

    for sm in db.get_all_social():
        button.insert(InlineKeyboardButton(text=sm[0], url=sm[1]))
        return button

# async def products_keyboard():
#     fff = db.get_data_series()
#     raqam = int (f"{fff[0]}")
#     murkup = InlineKeyboardMurkup(row_width=raqam)

#     product = db.get_mahsulot()
#     for product in products:
#       button_text = f"mahsulot: {product [0]}"
#       callback_data = f"mahsulot: {product [0]}"


#     markup.insert(
#          InlineKeyboardButton(text = button_text, callback_data)
# )
# return markup

@dp.callback_query_handler(text_contains="back_to_main_menu")
async def back_to_main_menu_method(call: types.CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.delete()
    await call.message.answer(f"Kerakli bo'limni tanlang!", reply_markup=main_menu)


@dp.callback_query_handler(text_contains="order_course")
async def order_course(call: types.CallbackQuery):
    await call.answer(cache_time=1)
    await call.message.edit_text("Ismingizni kiriting")
    await UserState.rname.set()


@dp.message_handler(state=UserState.rname, content_types=types.ContentTypes.TEXT)
async def user_get_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer("Siz bilan bog'lanishimiz uchun telefon raqamingizni kiriting yoki jo'nating",
                         reply_markup=get_number)
    await UserState.rphone.set()


@dp.message_handler(state=UserState.rphone, content_types=types.ContentTypes.TEXT)
@dp.message_handler(state=UserState.rphone, content_types=types.ContentTypes.CONTACT)
async def user_get_number(message: types.Message, state: FSMContext):
    if message.content_type == types.ContentType.CONTACT:
        number = message.contact.phone_number
    else:
        number = message.text
    await state.update_data(number=number)
    await message.answer("Siz ushbu kurs haqida malumotga egamisiz?", reply_markup=yes_or_no)
    await UserState.user_have_experience.set()


@dp.callback_query_handler(text_contains="no", state=UserState.user_have_experience)
async def user_have_experience(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=1)
    data = await state.get_data()
    name = data.get("name")
    number = data.get("number")
    course_name = data.get("course_name")
    try:
        db.add_user_course(name=name, number=number, course_name=course_name)
    except Exception as e:
        print(e)
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"Kursga buyurtma berdi\n\nIsmi: {name}\nTelefon raqami: {number}\nKurs nomi: {course_name}")
    await call.message.edit_text("Sizning buyurtmangiz qabul qilindi!")
    await call.message.answer(f"Kerakli bo'limni tanlang!", reply_markup=main_menu)


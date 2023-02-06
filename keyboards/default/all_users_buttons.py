from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


get_number = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Telefon raqamni jo'natish", request_contact=True)
        ]
    ],
    resize_keyboard=True
)

menu_user = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎓 Kurslar"),
            KeyboardButton(text="📚 Kitoblar")
        ],
        [
            KeyboardButton(text="📍 Bizning manzil"),
            KeyboardButton(text="☎️ Aloqa")
        ]
    ],
    resize_keyboard=True
)
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


first = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📚 Kitoblar"),
            KeyboardButton(text="🎓 Kurslar")
        ],
        [
            KeyboardButton(text="📍 Bizning manzil"),
            KeyboardButton(text="☎️ Aloqa")
        ],
        [
            KeyboardButton(text="📤 Post yuborish"),
            KeyboardButton(text="⚙️ Botni tahrirlash")
        ]
    ],
    resize_keyboard=True
)

tasdiq = ReplyKeyboardMarkup (
    keyboard=[
        [
            KeyboardButton(text="✅ ha"),
            KeyboardButton(text="❌ yo'q")
        ]
    ],
    resize_keyboard=True,

)

edit_menu = ReplyKeyboardMarkup (
    keyboard=[
        [
            KeyboardButton(text="🎓 Kurslar bo'limi"),
            KeyboardButton(text="📚 Kitoblar bo'limi")
        ],
        [
            KeyboardButton(text="🔙 Ortga")
        ]
    ],
    resize_keyboard=True
)



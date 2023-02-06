from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

answer_callback = CallbackData("answer","item_name")





main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📝 Kursga yozilish", callback_data="order_course"),
            InlineKeyboardButton(text="📚 Kurslar", callback_data="show_courses")
        ],
        [
            InlineKeyboardButton(text="🌐 Ijtimoiy tarmoqlar", callback_data="social")
        ]
    ]
)

back_to_main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📝 Kursga yozilish", callback_data="order_course")
        ],
        [
            InlineKeyboardButton(text="🏠 Asosiy menyuga qaytish", callback_data="back_to_main_menu"),
        ]
    ]
)

yes_or_no = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="yo'q", callback_data="no")
        ]
    ]
)

get_result = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Natijani olish", callback_data="get_result")
        ]
    ],
),


ansdict = {
    "✔ ha":"yes",
    "❌ yo'q":"no"
}




answerKey = InlineKeyboardMarkup(row_width=2)
for key, value in ansdict.items():
    answerKey.insert(InlineKeyboardButton(text=key, callback_data=answer_callback.new(item_name=value)))



location = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Google orqali borish", url="https://maps.google.com/maps?q=41.322438,69.282958&ll=41.322438,69.282958&z=16")
        ],
        [
            InlineKeyboardButton(text="Yandex orqali borish", url="https://yandex.com/navi/?whatshere%5Bpoint%5D=69.282847%2C41.322623&whatshere%5Bzoom%5D=18")
        ]
    ]
)



contact = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👨🏻‍💻 Admin", url="https://t.me/fbaacademy_admin"),
            InlineKeyboardButton(text="📲 Telegram", url="https://t.me/fbaacademyuz"),
        ],
        [
            InlineKeyboardButton(text="📲 Instagram", url="https://instagram.com/fbaacademyuz"),
            InlineKeyboardButton(text="📲 Facebook", url="https://facebook.com/fbaacademyuz"),
        ],
        [
            InlineKeyboardButton(text="📲 YouTube", url="https://www.youtube.com/channel/UCrTiDs9OBhtPG2T3-MNVsbg"),
            InlineKeyboardButton(text="✉️ Ulashish", switch_inline_query="Zo'r bot ekan"),
        ],
    ]
)

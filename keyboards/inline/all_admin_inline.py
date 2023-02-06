from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="➕ Yangi Kurs qo'shish", callback_data="admin_add_course"),
            InlineKeyboardButton(text="❌ Kursni o'chirish", callback_data="admin_delete_course")
        ],
    ]
)

admin_main_social = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="➕ Kitob qo'shish", callback_data="admin_add_book"),
            InlineKeyboardButton(text="❌ Kitob o'chirish", callback_data="admin_delete_book")
        ],
    ]
)



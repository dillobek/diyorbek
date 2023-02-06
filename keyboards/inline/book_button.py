from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import db

def pdf_button():
    markup = InlineKeyboardMarkup(row_width=2)
    datas = db.get_pdfs()
    # print (datas)
    for data in datas:
        markup.insert(InlineKeyboardButton(text=f"{data[1]}", callback_data=f"pdf:{data[0]}"))

    return markup
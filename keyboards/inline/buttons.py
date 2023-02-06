from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import db

def videos_button():
    markup = InlineKeyboardMarkup(row_width=2)
    datas = db.get_videos()
    # print(datas)
    for data in datas:
        markup.insert(InlineKeyboardButton(text=f"{data[1]}", callback_data=f"video:{data[0]}"))
    return markup

def remove_course():
    markup = InlineKeyboardMarkup(row_width=2)
    datas = db.get_videos()
    for data in datas:
        markup.insert(InlineKeyboardButton(text=f"{data[1]}", callback_data=f"del:{data[0]}"))
    return markup

def remove_pdf():
    markup = InlineKeyboardMarkup(row_width=2)
    datas = db.get_pdfs()
    for data in datas:
        markup.insert(InlineKeyboardButton(text=f"{data[1]}", callback_data=f"pdf:{data[0]}"))
    return markup



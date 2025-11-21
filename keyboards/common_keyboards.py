from gc import callbacks

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

BUTTON_LABEL = "ℹ️ Познать мудрость Лозы!"

def get_on_start_keyboard():
    builder = ReplyKeyboardBuilder() ##InlineKeyboardBuilder()
    builder.button(text=BUTTON_LABEL)

    return builder.as_markup(resize_keyboard=True)
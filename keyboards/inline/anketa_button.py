from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

from data.config import WEB_APP_URL

questionnaire_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Yo'riqnoma",
                callback_data='documentation'
            ),
            InlineKeyboardButton(
                text='Anketa',
                callback_data='questionare',
            )
        ]
    ]
)

questionare = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Anketa to'ldirish",
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]
    ]
)

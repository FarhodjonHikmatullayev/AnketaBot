from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

contact_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[
        [
            KeyboardButton(
                text="📞 Telefon raqamingizni yuboring",
                request_contact=True
            )
        ]
    ]
)

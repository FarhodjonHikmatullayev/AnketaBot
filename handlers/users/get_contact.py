from aiogram import types

from handlers.users.main_function import start_main_function
from loader import dp, db


@dp.message_handler(content_types='contact')
async def get_contact(message: types.Message):
    contact = message.contact
    phone = contact.phone_number
    user_id = contact.user_id
    first_name = contact.first_name
    last_name = contact.last_name
    username = message.from_user.username

    await db.create_user(
        phone=phone,
        username=username,
        telegram_id=user_id,
        first_name=first_name,
        last_name=last_name
    )

    text = "Siz muvofaqiyatli ro'yxatdan o'tdingiz!"
    await message.answer(text=text)

    # start bot main function
    await start_main_function(message)

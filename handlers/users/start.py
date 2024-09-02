from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from handlers.users.main_function import start_main_function
from keyboards.default.share_contact_keyboard import contact_keyboard
from loader import dp, db


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(f"Salom, {message.from_user.full_name}!")

    user_telegram_id = message.from_user.id
    user = await db.select_users(telegram_id=user_telegram_id)

    if user:
        # start bot main function
        await start_main_function(message)
    else:
        text = "📞 Telefon raqamingizni yuboring tugmasi orqali telefon raqamingizni yuboring."
        await message.answer(text=text, reply_markup=contact_keyboard)

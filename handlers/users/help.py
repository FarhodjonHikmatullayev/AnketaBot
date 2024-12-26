from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "�^=^s� Anketani telegram orqali to'ldirishda muammo bo'layotgan bo'lsa ushbu \nhttps://anketa.mega-center.uz/ sahifasiga \no'tib anketani to'ldiring")

    await message.answer("\n".join(text))

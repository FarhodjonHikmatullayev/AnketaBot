import json

from aiogram import types
from aiogram.types import ContentType

from keyboards.inline.anketa_button import questionare
from loader import dp


@dp.callback_query_handler(text="questionare")
async def questionare_filter(call: types.CallbackQuery):
    text = "📄 «Anketa to'ldirish» tugmasini bosish orqali siz anketa bo'limiga o'tqazilasiz. Anketa bo'limidagi barcha so'ralgan savollarga to'liq, aniq va xatolarsiz javob yozishingizni so'raymiz!"
    await call.message.answer(text=text, reply_markup=questionare)


@dp.message_handler(content_types=ContentType.WEB_APP_DATA)
async def start_questionare(message: types.Message):
    data = json.loads(message.web_app_data.data)  # JSON ma'lumotlarini o'qish
    print(data)  # Konsolga chiqarish
    await message.answer(f"Qabul qilingan ma'lumotlar: {data}")  # Foydalanuvchiga javob berish

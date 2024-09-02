from aiogram import types

from keyboards.inline.anketa_button import questionare
from loader import dp


@dp.callback_query_handler(text="documentation")
async def set_documentation(call: types.CallbackQuery):
    text = ("Foydalanish qoidalari:\n"
            "1. Siz barcha ma'lumotlarni to'liq kiritishingiz shart. Sizning kiritgan ma'lumotlaringiz xavfsizligi kafolatlanadi\n"
            "2. Ba'zi ma'lumotlarni botning o'zidagi tugmacha(knopka) orqali kiritishingiz kerak, masalan: filial, lavozim, ma'lumotingiz v.hkz shunga ahamiyat bering\n"
            "3. Ma'lumot kiritishda xato qilmaslikka harakat qiling\n"
            "4. Kiritgan ma'lumotlaringizni tasdiqlashdan oldin to'g'ri kiritganingizga ishonch hosil qilish uchun tekshirib chiqing\n"
            "5.Start tugmasini bosishingiz bilan bizga yuborgan malumotlaringizdan foydalanishga ruhsat bergan bo'lasiz. Biz shu ma'lumotlar orqali siz bilan bog'lanamiz\n"
            " Omadingizni bersin...")
    await call.message.answer(text=text)

from keyboards.inline.anketa_button import questionnaire_keyboard


async def start_main_function(message):
    text = ("Salom 👋🏻\n"
            "Bu yerda siz o‘zingizning arizangizni 📄 to‘ldirishingiz va bizning kompaniyamizdagi mavjud bo‘sh ish o‘rinlari haqida bilib olishingiz mumkin!\n"
            "\n"
            "Здравствуйте 👋🏻\n"
            "Здесь Вы можете заполнить свою анкету 📄 и узнать о существующих вакансиях нашей Компании!")

    await message.answer(text=text, reply_markup=questionnaire_keyboard)

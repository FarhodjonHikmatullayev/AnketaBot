from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=221, null=True, blank=True)
    last_name = models.CharField(max_length=221, null=True, blank=True)
    username = models.CharField(max_length=221, null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    telegram_id = models.BigIntegerField(unique=True)

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Foydalanuvchilar'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Questionnaire(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Ism")
    last_name = models.CharField(max_length=100, verbose_name="Familiya")
    birth_date = models.DateField(verbose_name="Tug'ilgan sana")
    gender = models.CharField(max_length=10, verbose_name="Jinsi")
    marital_status = models.CharField(max_length=221)
    education_institutions = models.CharField(max_length=200,
                                              verbose_name="Ta'lim muassasalari nomi va bitirgan yilingiz")  # ko'p bo'lishi mumkin
    height_weight = models.CharField(max_length=20, verbose_name="Bo'y va vazningiz (sm/kg)")
    languages = models.TextField(blank=True, verbose_name="Qaysi tillarni bilasiz? va qay darajada")
    region = models.CharField(max_length=100, verbose_name="Viloyat (Haqiqiy turar joy)")
    city_district = models.CharField(max_length=100, verbose_name="Shaxar/Tuman (Haqiqiy turar joy)")
    address = models.CharField(max_length=200, verbose_name="Manzilingiz (MFY, ko'cha)")
    desired_branch = models.CharField(max_length=100, verbose_name="Qaysi filialda ishlashni xohlaysiz?")
    desired_position = models.CharField(max_length=100, verbose_name="Qaysi lavozimda ishlashni xohlaysiz?")
    worked_before = models.BooleanField(default=False, verbose_name="Avval bizning kompaniyamizda ishlaganmisiz?")
    is_citizen = models.BooleanField(default=True, verbose_name="O'zbekiston Respublikasi fuqarosimisiz?")
    is_employed = models.BooleanField(default=False, verbose_name="Hozirda ish bilan ta'minlangamisiz?")
    relative_in_company = models.BooleanField(default=False,
                                              verbose_name="Bizdang kompaniyada ishlaydigan yaqin qarindoshingiz bormi?")
    software_skills = models.TextField(blank=True, verbose_name="Qaysi dasturlardan foydalana olasiz? va qay darajada")
    health_info = models.TextField(blank=True, verbose_name="Sog'ligingiz xaqida ma'lumotlar")
    previous_job = models.CharField(max_length=221, verbose_name="Oxirgi ish joyingiz", null=True, blank=True)
    last_salary = models.DecimalField(max_digits=10, decimal_places=2,
                                      verbose_name="Oxirgi ish joyida olgan ish xaqingiz (so'm)?", null=True,
                                      blank=True)
    desired_salary = models.DecimalField(max_digits=10, decimal_places=2,
                                         verbose_name="Qancha maosh olishni xohlaysiz (so'm)?", null=True, blank=True)
    has_personal_car = models.BooleanField(default=False, verbose_name="Shaxsiy avtomobilingiz bormi?")
    can_travel = models.BooleanField(default=False, verbose_name="Xizmat safariga bora olasizmi?")
    job_source = models.CharField(max_length=200, verbose_name="Bo'sh ish o'rni haqida qayerdan bildingiz?")
    working_period = models.CharField(max_length=500,
                                      verbose_name="Bizning kompaniyada qancha vaqt mobaynida ishlamoqchisiz?")
    personal_phone = models.CharField(max_length=20, verbose_name="Shaxsiy telefon raqam")
    additional_phone = models.CharField(max_length=20, verbose_name="Qo'shimcha telefon raqam", blank=True)
    personal_photo = models.ImageField(upload_to='temp/', verbose_name="Shaxsiy rasmingiz *", null=True, blank=True)
    family_member = models.TextField(verbose_name="Oila a'zolari haqida ma'lumotlar")
    passport_type = models.CharField(max_length=20, verbose_name="Pasport turi")
    passport_image = models.ImageField(upload_to='temp/',
                                       verbose_name="Pasport rasmi (yoki ID card)", null=True, blank=True)
    id_card_back_photo = models.ImageField(upload_to='temp/',
                                           verbose_name="ID card orqa tomon rasmi", null=True, blank=True)
    id_card_front_photo = models.ImageField(upload_to='temp/', null=True, blank=True,
                                            verbose_name="ID card old tomon rasmi")
    difficulty = models.CharField(max_length=20, verbose_name="Anketaning qiyinlik darajasi")
    consent = models.BooleanField(default=False, verbose_name="Roziman * (Rozilik shartlari bilan tanishish)")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    response = models.CharField(max_length=500, null=True, blank=True,
                                verbose_name="Agar 10 kun davomida sizga qayta aloqaga chiqmasak bu lavozimga ehtiyojimiz yo'qligini bildiradi. Tanlang:")
    pdf_file = models.FileField(upload_to='pdfs/', null=True, blank=True, verbose_name='PDF fayl')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Yuborilgan vaqt")

    class Meta:
        db_table = 'questionnaire'
        verbose_name = 'Questionnaire'
        verbose_name_plural = 'Anketalar'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# class Application(models.Model):
#     first_name = models.CharField(max_length=50, null=True, verbose_name='Ism')
#     last_name = models.CharField(max_length=50, null=True, verbose_name='Familiya')
#     pdf_file = models.FileField(upload_to='pdfs/', null=True, blank=True, verbose_name='PDF fayl')
#     created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Yuborilgan vaqt")
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
#
#     class Meta:
#         db_table = 'application'
#         verbose_name = 'Application'
#         verbose_name_plural = 'Anketalar'
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

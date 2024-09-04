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
    father_name = models.CharField(max_length=100, verbose_name="Otasining ismi")
    birth_date = models.DateField(verbose_name="Tug'ilgan sana")
    gender = models.CharField(max_length=10, choices=[('male', 'Erkak'), ('female', 'Ayol')], verbose_name="Jinsi")
    marital_status = models.CharField(max_length=20,
                                      choices=[('single', 'Turmush qurmagan'), ('married', 'Turmush qurgan'),
                                               ('devorced', 'Ajrashgan')], verbose_name="Oilaviy xolatingiz")
    education_institution = models.CharField(max_length=200,
                                             verbose_name="Ta'lim muassasalari nomi va bitirgan yilingiz")  # ko'p bo'lishi mumkin
    height_weight = models.CharField(max_length=20, verbose_name="Bo'y va vazningiz (sm/kg)")
    is_student = models.BooleanField(default=False,
                                     verbose_name="Siz hozirda qaysidir universitet, litsey yoki kollej talabasimisiz?")
    languages = models.TextField(blank=True, verbose_name="Qaysi tillarni bilasiz?")
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
    software_skills = models.TextField(blank=True, verbose_name="Qaysi dasturlardan foydalana olasiz?")
    health_info = models.TextField(blank=True, verbose_name="Sog'ligingiz xaqida ma'lumotlar")
    last_salary = models.DecimalField(max_digits=10, decimal_places=2,
                                      verbose_name="Oxirgi ish joyida olgan ish xaqingiz (so'm)?", null=True,
                                      blank=True)
    desired_salary = models.DecimalField(max_digits=10, decimal_places=2,
                                         verbose_name="Qancha maosh olishni xohlaysiz (so'm)?", null=True, blank=True)
    has_personal_car = models.BooleanField(default=False, verbose_name="Shaxsiy avtomobilingiz bormi?")
    car_model = models.CharField(max_length=100, verbose_name="Avtomabilingiz rusumi", blank=True)
    can_travel = models.BooleanField(default=False, verbose_name="Xizmat safariga bora olasizmi?")
    job_source = models.CharField(max_length=200, verbose_name="Bo'sh ish o'rni haqida qayerdan bildingiz?")
    has_criminal_record = models.BooleanField(default=False, verbose_name="Sudlanganmisiz?")
    criminal_record_details = models.TextField(blank=True,
                                               verbose_name="Sudlanganligingiz (Qaysi moddalar bo'yicha)")  # ishlash kerak
    additional_phone = models.CharField(max_length=20, verbose_name="Qo'shimcha telefon raqam", blank=True)
    personal_photo = models.ImageField(upload_to='Project/photos/', verbose_name="Shaxsiy rasmingiz *")
    passport_type = models.CharField(max_length=20, choices=[('passport', 'Pasport'), ('id_card', 'ID karta')],
                                     verbose_name="Pasport turi")
    passport_photo = models.ImageField(upload_to='Project/passport_photos/',
                                       verbose_name="Pasport rasmi (yoki ID card)")
    id_card_back_photo = models.ImageField(upload_to='Project/id_card_back_photos/',
                                           verbose_name="ID card orqa tomon rasmi")
    consent = models.BooleanField(default=False, verbose_name="Roziman * (Rozilik shartlari bilan tanishish)")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        db_table = 'questionnaire'
        verbose_name = 'Questionnaire'
        verbose_name_plural = 'Anketalar'


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

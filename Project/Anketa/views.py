from datetime import datetime
from decimal import Decimal
from django.views.decorators.csrf import csrf_protect
import io
from reportlab.pdfgen import canvas
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render
from reportlab.lib.pagesizes import letter
import os
from .models import Questionnaire


@csrf_protect
def questionnaire_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        birth_date = request.POST.get('birth_date')
        gender = request.POST.get('gender')
        marital_status = request.POST.get('marital_status')
        education_institutions = request.POST.getlist('education_institution[]')
        graduation_years = request.POST.getlist('graduation_year[]')
        language = request.POST.getlist('language[]')
        language_level = request.POST.getlist('language_level[]')
        region = request.POST.get('region')
        city_district = request.POST.get('city_district')
        address = request.POST.get('address')
        desired_branches = request.POST.getlist('desired_branch[]')
        desired_position = request.POST.getlist('desired_position')
        worked_before = request.POST.get('worked_before') == 'true'
        is_citizen = request.POST.get('is_citizen') == 'true'
        is_employed = request.POST.get('is_employed') == 'true'
        previous_job = request.POST.get('previous_job')
        try:
            previous_salary = float(request.POST.get('previous_salary', '0'))
        except:
            previous_salary = 0
        print("type(desired_salary)", type(previous_salary))
        relative_in_company = request.POST.get('relative_in_company') == 'true'
        software = request.POST.getlist('software[]')
        software_level = request.POST.getlist('software_level[]')
        health_info = request.POST.get('health_info')
        try:
            desired_salary = float(request.POST.get('desired_salary', '0'))
        except:
            desired_salary = 0
        print("type(desired_salary)", type(desired_salary))
        has_personal_car = request.POST.get('has_personal_car') == 'true'
        can_travel = request.POST.get('can_travel') == 'true'
        job_source = request.POST.get('job_source')
        working_period = request.POST.get('working_period')
        personal_phone = request.POST.get('personal_phone')
        additional_phone = request.POST.get('additional_phone')
        family_member = request.POST.getlist('family_member[]')
        family_name = request.POST.getlist('family_name[]')
        family_birth_date = request.POST.getlist('family_birth_date[]')
        job_title = request.POST.getlist('job_title[]')
        personal_photo = request.FILES.get('personal_photo')
        passport_type = request.POST.get('passport_type')
        passport_image = request.FILES.get('passport_image')
        id_card_front = request.FILES.get('id_card_front')
        id_card_back = request.FILES.get('id_card_back')
        difficulty = request.POST.get('difficulty')
        consent = request.POST.get('consent') == 'on'
        height_weight = request.POST.get('height_weight')
        response = request.POST.get('response')

        buffer = io.BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        p.setFont("Helvetica", 12)
        y = 750
        line_height = 20

        def draw_string(p, text, y):
            if y < 40:
                p.showPage()
                p.setFont("Helvetica", 12)
                return 750, True
            p.drawString(100, y, text)
            return y - line_height, False

        # Asosiy ma'lumotlar
        birth_date = birth_date.split('-')
        y, new_page = draw_string(p, f"Ism: {request.POST.get('first_name').capitalize()}", y)
        y, new_page = draw_string(p, f"Familiya: {request.POST.get('last_name').capitalize()}", y)
        y, new_page = draw_string(p, f"Tug'ilgan sanangiz: {birth_date[-1]}.{birth_date[-2]}.{birth_date[0]}", y)
        y, new_page = draw_string(p, f"Jinsingiz: {request.POST.get('gender')}", y)
        y, new_page = draw_string(p, f"Oilaviy holatingiz: {request.POST.get('marital_status')}", y)
        y, new_page = draw_string(p, f"Viloyat: {request.POST.get('region').capitalize()}", y)
        y, new_page = draw_string(p, f"Shahar/Tuman: {request.POST.get('city_district').capitalize()}", y)
        y, new_page = draw_string(p, f"Manzil: {request.POST.get('address')}", y)
        y, new_page = draw_string(p,
                                  f"Qaysi filiallarda ishlamoqchisiz: {', '.join(request.POST.getlist('desired_branch[]'))}",
                                  y)
        y, new_page = draw_string(p, f"Qanday lavozimda ishlamoqchisiz: {request.POST.getlist('desired_position')[0]}",
                                  y)
        # is_citizen
        y, new_page = draw_string(p, f"Shaxsiy telefon: {request.POST.get('personal_phone')}", y)
        y, new_page = draw_string(p, f"Qo'shimcha telefon: {request.POST.get('additional_phone')}", y)

        # Ta'lim
        y, new_page = draw_string(p, "* Ta'lim muassasalari:", y)
        talim = ""
        for institution, year in zip(request.POST.getlist('education_institution[]'),
                                     request.POST.getlist('graduation_year[]')):
            y, new_page = draw_string(p, f"{institution} - {year}", y)
            talim += f"{institution} - {year}\n"

        # Biladigan tillar
        tillar = ""
        y, new_page = draw_string(p, "* Biladigan tillari:", y)
        for lang, level in zip(request.POST.getlist('language[]'), request.POST.getlist('language_level[]')):
            y, new_page = draw_string(p, f"{lang} - {level}", y)
            tillar += f"{lang} - {level}\n"

        # Biladigan dasturlar
        dasturlar = ""
        y, new_page = draw_string(p, "* Biladigan dasturlari:", y)
        for soft, level in zip(request.POST.getlist('software[]'), request.POST.getlist('software_level[]')):
            y, new_page = draw_string(p, f"{soft} - {level}", y)
            dasturlar += f"{soft} - {level}\n"

        # Oilaviy a'zolar
        oila = ""
        y, new_page = draw_string(p, " * Oila a'zolari:", y)
        for member, name, birth, job in zip(request.POST.getlist('family_member[]'),
                                            request.POST.getlist('family_name[]'),
                                            request.POST.getlist('family_birth_date[]'),
                                            request.POST.getlist('job_title[]')):
            birth = birth.split('-')
            birth[0], birth[-1] = birth[-1], birth[0]
            y, new_page = draw_string(p, f"{member} - {name} - {'.'.join(birth)} - {job}", y)
            oila += f"{member} - {name} - {'.'.join(birth)} - {job}\n"

        # Boshqa ma'lumotlar
        y, new_page = draw_string(p,
                                  f"Oldin bizning kompaniyada ishlaganmisiz: {'Ha' if request.POST.get('worked_before') == 'true' else 'Yoq'}",
                                  y)
        y, new_page = draw_string(p,
                                  f"O'zbekiston fuqarosimisiz: {'Ha' if request.POST.get('is_citizen') == 'true' else 'Yoq'}",
                                  y)
        y, new_page = draw_string(p,
                                  f"Ilgari biror joyda ishlaganmisiz: {'Ha' if request.POST.get('is_employed') == 'true' else 'Yoq'}",
                                  y)
        if request.POST.get('is_employed') == 'true':
            y, new_page = draw_string(p, f"Oldingi ish joyingiz: {request.POST.get('previous_job')}", y)
            y, new_page = draw_string(p, f"Oldingi maoshingiz: {request.POST.get('previous_salary')}", y)
        y, new_page = draw_string(p,
                                  f"Bizdang kompaniyada ishlaydigan yaqin qarindoshingiz bormi: {'Ha' if request.POST.get('relative_in_company') == 'true' else 'Yoq'}",
                                  y)
        y, new_page = draw_string(p, f"Sog'lig'ingiz haqida ma'lumot: {request.POST.get('health_info')}", y)
        y, new_page = draw_string(p, f"Qancha maosh olishni xohlaysiz (so'm): {request.POST.get('desired_salary')}", y)
        y, new_page = draw_string(p,
                                  f"Shaxsiy avtomobilingiz bormi: {'Ha' if request.POST.get('has_personal_car') == 'true' else 'Yoq'}",
                                  y)

        p.showPage()
        p.setFont("Helvetica", 12)  # Yangi sahifada shriftni qayta o'rnating
        y = 750

        y, new_page = draw_string(p,
                                  f"Xizmat safariga bora olasizmi: {'Ha' if request.POST.get('can_travel') == 'true' else 'Yoq'}",
                                  y)
        y, new_page = draw_string(p, f"Bo'sh ish o'rni haqida qayerdan bildingiz: {request.POST.get('job_source')}", y)
        y, new_page = draw_string(p, f"Bizda qancha vaqt ishlamoqchisiz: {request.POST.get('working_period')}", y)
        y, new_page = draw_string(p,
                                  f"Bu anketani to'ldirish sizga qiyinlik tug'dirmadimi: {request.POST.get('difficulty')}",
                                  y)
        y, new_page = draw_string(p, f"Rozilik: {'Ha' if request.POST.get('consent') == 'on' else 'Yoq'}", y)
        y, new_page = draw_string(p, f"Bo'y va vazn: {request.POST.get('height_weight')}", y)
        y, new_page = draw_string(p,
                                  f"Agar 10 kun davomida sizga qayta aloqaga chiqmasak bu lavozimga ehtiyojimiz yo'qligini bildiradi. Tanlang: {request.POST.get('response')}",
                                  y)

        images = [
            (request.FILES.get('personal_photo'), "* Shaxsiy rasmi"),
            (request.FILES.get('passport_image'), "* Pasport rasmi"),
            (request.FILES.get('id_card_front'), "* ID kartaning old tomoni"),
            (request.FILES.get('id_card_back'), "* ID kartaning orqa tomoni")
        ]
        y_position = y - 20  # Birinchi rasm uchun boshlanish joyi

        for img, label in images:
            if img:
                y_position, new_page = draw_string(p, label, y_position)

                temp_file_path = default_storage.save(f'temp/{img.name}', img)
                temp_file_full_path = default_storage.path(temp_file_path)

                p.drawImage(temp_file_full_path, 100, y_position - 200, width=200, height=200)

                # os.remove(temp_file_full_path)

                y_position -= 250  # Move down for the next image

                if y_position < 40:
                    p.showPage()
                    p.setFont("Helvetica", 12)
                    y_position = 750

        p.save()
        buffer.seek(0)
        pdf_file = ContentFile(buffer.getvalue(), f"{first_name}_{last_name}.pdf")
        birth_date = datetime.strptime(request.POST.get('birth_date'), '%Y-%m-%d').date()

        # try:
        questionnaire = Questionnaire(
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            gender=gender,
            marital_status=marital_status,
            education_institutions=talim,
            languages=tillar,
            region=region,
            city_district=city_district,
            address=address,
            desired_branch=', '.join(desired_branches),
            desired_position=desired_position[0],
            worked_before=worked_before,
            is_citizen=is_citizen,
            is_employed=is_employed,
            previous_job=previous_job,
            last_salary=previous_salary,
            relative_in_company=relative_in_company,
            software_skills=dasturlar,
            health_info=health_info,
            desired_salary=desired_salary,
            has_personal_car=has_personal_car,
            can_travel=can_travel,
            job_source=job_source,
            working_period=working_period,
            personal_phone=personal_phone,
            additional_phone=additional_phone,
            family_member=oila,
            personal_photo=personal_photo,
            passport_type=passport_type,
            passport_image=passport_image,
            id_card_front_photo=id_card_front,
            id_card_back_photo=id_card_back,
            difficulty=difficulty,
            consent=consent,
            height_weight=height_weight,
            response=response,
            pdf_file=pdf_file,
        )
        questionnaire.save()
        # except Exception as e:
        #     print(e)

        return render(request, template_name='success.html')
    return render(request, 'form.html')

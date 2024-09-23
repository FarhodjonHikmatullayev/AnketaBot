from django.views.decorators.csrf import csrf_protect
import io
from reportlab.pdfgen import canvas
from django.core.files.base import ContentFile

from django.shortcuts import render, redirect, get_object_or_404
from reportlab.lib.pagesizes import letter

from .models import Application


@csrf_protect
def questionnaire_view(request):
    if request.method == 'POST':
        print(request.POST)
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
        desired_position = request.POST.getlist('desired_position[]')
        worked_before = request.POST.get('worked_before') == 'on'
        is_citizen = request.POST.get('is_citizen') == 'on'
        is_employed = request.POST.get('is_employed') == 'on'
        previous_job = request.POST.get('previous_job')
        previous_salary = request.POST.get('previous_salary')
        relative_in_company = request.POST.get('relative_in_company') == 'on'
        software = request.POST.getlist('software[]')
        software_level = request.POST.getlist('software_level[]')
        health_info = request.POST.get('health_info')
        desired_salary = request.POST.get('desired_salary')
        has_personal_car = request.POST.get('has_personal_car') == 'on'
        can_travel = request.POST.get('can_travel') == 'on'
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
        passport_image = request.POST.get('passport_image')
        id_card_front = request.POST.get('id_card_front')
        id_card_back = request.POST.get('id_card_back')
        difficulty = request.POST.get('difficulty')
        consent = request.POST.get('consent') == 'on'
        height_weight = request.POST.get('height_weight')
        response = request.POST.get('response')



        buffer = io.BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        p.setFont("Helvetica", 12)

        # Asosiy ma'lumotlar
        p.drawString(100, 750, f"Ism: {first_name}")
        p.drawString(100, 730, f"Familiya: {last_name}")
        p.drawString(100, 710, f"Tug'ilgan sana: {birth_date}")
        p.drawString(100, 690, f"Jinsi: {gender}")
        p.drawString(100, 670, f"Oilaviy holati: {marital_status}")
        p.drawString(100, 650, f"Viloyat: {region}")
        p.drawString(100, 630, f"Shahar/Tuman: {city_district}")
        p.drawString(100, 610, f"Manzil: {address}")
        p.drawString(100, 590, f"Shaxsiy telefon: {personal_phone}")
        p.drawString(100, 570, f"Qo'shimcha telefon: {additional_phone}")

        # Ta'lim
        p.drawString(100, 550, "Ta'lim:")
        y = 530
        for institution, year in zip(education_institutions, graduation_years):
            p.drawString(120, y, f"{institution} - {year}")
            y -= 20

        # Biladigan tillar
        p.drawString(100, y, "Biladigan tillar:")
        y -= 20
        for lang, level in zip(language, language_level):
            p.drawString(120, y, f"{lang} - {level}")
            y -= 20

        # Biladigan dasturlar
        p.drawString(100, y, "Biladigan dasturlar:")
        y -= 20
        for soft, level in zip(software, software_level):
            p.drawString(120, y, f"{soft} - {level}")
            y -= 20

        # Oilaviy a'zolar
        p.drawString(100, y, "Oilaviy a'zolar:")
        y -= 20
        for member, name, birth, job in zip(family_member, family_name, family_birth_date, job_title):
            p.drawString(120, y, f"{member} - {name} - {birth} - {job}")
            y -= 20

        # Boshqa ma'lumotlar
        p.drawString(100, y, f"Oldin ishlagan: {'Ha' if worked_before else 'Yoq'}")
        y -= 20
        p.drawString(100, y, f"Fuqarolik: {'Ha' if is_citizen else 'Yoq'}")
        y -= 20
        p.drawString(100, y, f"Bandlik: {'Ha' if is_employed else 'Yoq'}")
        y -= 20
        p.drawString(100, y, f"Oldingi ish joyi: {previous_job}")
        y -= 20
        p.drawString(100, y, f"Oldingi maosh: {previous_salary}")
        y -= 20
        p.drawString(100, y, f"Kompaniyada qarindosh: {'Ha' if relative_in_company else 'Yoq'}")
        y -= 20
        p.drawString(100, y, f"Sog'liq haqida ma'lumot: {health_info}")
        y -= 20
        p.drawString(100, y, f"Istagan maosh: {desired_salary}")
        y -= 20
        p.drawString(100, y, f"Shaxsiy avtomobil: {'Ha' if has_personal_car else 'Yoq'}")
        y -= 20
        p.drawString(100, y, f"Safar qilish imkoniyati: {'Ha' if can_travel else 'Yoq'}")
        y -= 20
        p.drawString(100, y, f"Ish manbasi: {job_source}")
        y -= 20
        p.drawString(100, y, f"Ish davri: {working_period}")
        y -= 20
        p.drawString(100, y, f"Qiyinchilik: {difficulty}")
        y -= 20
        p.drawString(100, y, f"Rozilik: {'Ha' if consent else 'Yoq'}")
        y -= 20
        p.drawString(100, y, f"Bo'y va vazn: {height_weight}")
        y -= 20
        p.drawString(100, y, f"Javob: {response}")

        p.showPage()
        p.save()

        buffer.seek(0)
        pdf_file = ContentFile(buffer.getvalue(), f"{first_name}_{last_name}.pdf")
        application = Application(
            first_name=first_name,
            last_name=last_name,
            pdf_file=pdf_file
        )
        application.save()

        return render(request, template_name='success.html')
    return render(request, 'form.html')

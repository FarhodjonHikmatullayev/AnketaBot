from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Questionnaire
from django.shortcuts import render, redirect, get_object_or_404
from .models import Questionnaire


def questionnaire_view(request):
    if request.method == 'POST':
        # POST so'rovini olish
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        father_name = request.POST.get('father_name')
        birth_date = request.POST.get('birth_date')
        gender = request.POST.get('gender')
        marital_status = request.POST.get('marital_status')
        education_institution = request.POST.get('education_institution')
        height_weight = request.POST.get('height_weight')
        is_student = request.POST.get('is_student') == 'on'
        languages = request.POST.get('languages')
        region = request.POST.get('region')
        city_district = request.POST.get('city_district')
        address = request.POST.get('address')
        desired_branch = request.POST.get('desired_branch')
        desired_position = request.POST.get('desired_position')
        worked_before = request.POST.get('worked_before') == 'on'
        is_citizen = request.POST.get('is_citizen') == 'on'
        is_employed = request.POST.get('is_employed') == 'on'
        relative_in_company = request.POST.get('relative_in_company') == 'on'
        software_skills = request.POST.get('software_skills')
        health_info = request.POST.get('health_info')
        last_salary = request.POST.get('last_salary')
        desired_salary = request.POST.get('desired_salary')
        has_personal_car = request.POST.get('has_personal_car') == 'on'
        car_model = request.POST.get('car_model')
        can_travel = request.POST.get('can_travel') == 'on'
        job_source = request.POST.get('job_source')
        has_criminal_record = request.POST.get('has_criminal_record') == 'on'
        criminal_record_details = request.POST.get('criminal_record_details')
        additional_phone = request.POST.get('additional_phone')
        personal_photo = request.FILES.get('personal_photo')
        passport_type = request.POST.get('passport_type')
        passport_photo = request.FILES.get('passport_photo')
        id_card_back_photo = request.FILES.get('id_card_back_photo')
        consent = request.POST.get('consent') == 'on'

        questionnaire_instance = Questionnaire.objects.create(
            first_name=first_name,
            last_name=last_name,
            father_name=father_name,
            birth_date=birth_date,
            gender=gender,
            marital_status=marital_status,
            education_institution=education_institution,
            height_weight=height_weight,
            is_student=is_student,
            languages=languages,
            region=region,
            city_district=city_district,
            address=address,
            desired_branch=desired_branch,
            desired_position=desired_position,
            worked_before=worked_before,
            is_citizen=is_citizen,
            is_employed=is_employed,
            relative_in_company=relative_in_company,
            software_skills=software_skills,
            health_info=health_info,
            last_salary=last_salary,
            desired_salary=desired_salary,
            has_personal_car=has_personal_car,
            car_model=car_model,
            can_travel=can_travel,
            job_source=job_source,
            has_criminal_record=has_criminal_record,
            criminal_record_details=criminal_record_details,
            additional_phone=additional_phone,
            personal_photo=personal_photo,
            passport_type=passport_type,
            passport_photo=passport_photo,
            id_card_back_photo=id_card_back_photo,
            consent=consent
        )
        return render(request, template_name='success.html')
    return render(request, 'form.html')

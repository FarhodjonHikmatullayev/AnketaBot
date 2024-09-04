from django import forms
from .models import Questionnaire


class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = [
            'first_name', 'last_name', 'father_name', 'birth_date', 'gender',
            'marital_status', 'education_institution', 'height_weight',
            'is_student', 'languages', 'region', 'city_district', 'address',
            'desired_branch', 'desired_position', 'worked_before',
            'is_citizen', 'is_employed', 'relative_in_company',
            'software_skills', 'health_info', 'last_salary',
            'desired_salary', 'has_personal_car', 'car_model',
            'can_travel', 'job_source', 'has_criminal_record',
            'criminal_record_details', 'additional_phone',
            'personal_photo', 'passport_type', 'passport_photo',
            'id_card_back_photo', 'consent'
        ]
        # widgets = {
        #     'birth_date': forms.DateInput(attrs={'type': 'date'}),
        #     'personal_photo': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        #     'passport_photo': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        #     'id_card_back_photo': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        #     'languages': forms.Textarea(attrs={'rows': 3}),
        #     'software_skills': forms.Textarea(attrs={'rows': 3}),
        #     'health_info': forms.Textarea(attrs={'rows': 3}),
        #     'criminal_record_details': forms.Textarea(attrs={'rows': 3}),
        # }

# Generated by Django 5.1 on 2024-09-25 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Anketa', '0006_alter_application_options_alter_application_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Yuborilgan vaqt'),
        ),
    ]

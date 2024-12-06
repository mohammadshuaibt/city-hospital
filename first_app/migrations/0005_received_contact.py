# Generated by Django 5.1.2 on 2024-11-19 05:13

import first_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_alter_doctor_doc_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Received_Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email_address', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=13, validators=[first_app.models.validate_indian_phone_number])),
            ],
        ),
    ]
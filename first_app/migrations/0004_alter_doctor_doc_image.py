# Generated by Django 5.1.2 on 2024-11-16 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_alter_doctor_doc_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='doc_image',
            field=models.ImageField(upload_to='doctors/'),
        ),
    ]

# Generated by Django 5.1.2 on 2024-11-27 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0009_alter_department_dep_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='dep_image',
            field=models.FileField(default='default.jpg', upload_to='departments/'),
        ),
    ]

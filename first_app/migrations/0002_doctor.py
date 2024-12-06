# Generated by Django 5.1.2 on 2024-11-16 05:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=40)),
                ('doc_spec', models.TextField()),
                ('doc_image', models.ImageField(upload_to='doctors')),
                ('dept_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.department')),
            ],
        ),
    ]

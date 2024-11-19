# Generated by Django 5.1.3 on 2024-11-18 11:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('grades', '0001_initial'),
        ('students', '0001_initial'),
        ('users', '__first__'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student'),
        ),
        migrations.AddField(
            model_name='grade',
            name='teacher',
            field=models.ForeignKey(limit_choices_to={'role': 'Teacher'}, on_delete=django.db.models.deletion.CASCADE, to='users.customuser'),
        ),
    ]

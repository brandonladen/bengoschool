# Generated by Django 4.0.8 on 2023-05-21 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grading', '0002_gradinglevel_current'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gradinglevel',
            name='grading_rules',
        ),
        migrations.AddField(
            model_name='gradingrules',
            name='grading_level',
            field=models.ManyToManyField(to='grading.gradinglevel'),
        ),
    ]

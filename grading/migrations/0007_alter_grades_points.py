# Generated by Django 4.0.8 on 2023-05-21 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grading', '0006_grades_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grades',
            name='points',
            field=models.IntegerField(default=1),
        ),
    ]
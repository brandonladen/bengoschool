# Generated by Django 4.0.8 on 2023-05-21 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authman', '0006_alter_student_options_remove_student_firstname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
    ]

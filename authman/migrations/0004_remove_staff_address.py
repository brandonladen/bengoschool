# Generated by Django 4.2.1 on 2023-06-05 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authman', '0003_alter_staff_role_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='address',
        ),
    ]
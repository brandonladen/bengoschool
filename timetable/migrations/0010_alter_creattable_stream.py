# Generated by Django 4.2.1 on 2023-06-04 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0002_alter_studentclass_sections'),
        ('timetable', '0009_alter_creattable_stream'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creattable',
            name='stream',
            field=models.ForeignKey(blank=True, default='Custom', help_text='Select custom if class has no sections', null=True, on_delete=django.db.models.deletion.CASCADE, to='academics.classsection'),
        ),
    ]
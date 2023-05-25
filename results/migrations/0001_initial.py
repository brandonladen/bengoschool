# Generated by Django 4.0.8 on 2023-05-25 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authman', '0001_initial'),
        ('academics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_score', models.IntegerField(default=0)),
                ('exam_score', models.IntegerField(default=0)),
                ('points_earned', models.PositiveIntegerField(default=0)),
                ('current_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.studentclass')),
                ('current_section', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='academics.classsection')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.academicsession')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authman.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authman.subject')),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.academicterm')),
            ],
            options={
                'ordering': ['subject'],
            },
        ),
    ]

# Generated by Django 2.2.3 on 2019-07-22 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_courses'),
        ('userhandling', '0001_initial'),
        ('studentpanel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseEnrolled',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Courses')),
                ('studentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userhandling.Users')),
            ],
        ),
    ]

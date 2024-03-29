# Generated by Django 2.2.3 on 2019-07-22 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userhandling', '0001_initial'),
        ('web', '0002_assignment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('courseCode', models.CharField(max_length=20)),
                ('courseTitle', models.CharField(max_length=50)),
                ('semester', models.CharField(max_length=50)),
                ('enrollmentKey', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userhandling.Users')),
            ],
        ),
    ]

# Generated by Django 2.2.1 on 2019-06-25 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignmenttitle', models.CharField(max_length=150)),
                ('details', models.CharField(max_length=200)),
                ('deadline', models.CharField(max_length=30)),
            ],
        ),
    ]

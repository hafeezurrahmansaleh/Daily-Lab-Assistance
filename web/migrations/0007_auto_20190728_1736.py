# Generated by Django 2.2.2 on 2019-07-28 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20190728_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='teacherId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userhandling.Users'),
        ),
    ]

# Generated by Django 2.1.2 on 2018-10-16 08:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20181016_0147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='date_create',
        ),
        migrations.AddField(
            model_name='notes',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 16, 8, 42, 32, 62396)),
        ),
    ]
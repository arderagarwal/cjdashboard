# Generated by Django 2.0.6 on 2018-06-19 07:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recruitertests', '0003_auto_20180619_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 19, 7, 57, 7, 840692, tzinfo=utc)),
        ),
    ]

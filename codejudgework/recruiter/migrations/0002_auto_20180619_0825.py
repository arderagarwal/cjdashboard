# Generated by Django 2.0.6 on 2018-06-19 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruiter',
            name='PhoneNo',
            field=models.BigIntegerField(),
        ),
    ]

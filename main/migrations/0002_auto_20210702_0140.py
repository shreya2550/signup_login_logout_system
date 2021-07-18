# Generated by Django 3.1.12 on 2021-07-01 20:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiary',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MaxLengthValidator(3), django.core.validators.MinLengthValidator(2)]),
        ),
    ]
# Generated by Django 3.1.7 on 2021-05-05 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cvision', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='Description',
            field=models.CharField(default='Описание отсутствует', max_length=1500, verbose_name='description'),
        ),
    ]
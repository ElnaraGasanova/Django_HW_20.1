# Generated by Django 5.0.2 on 2024-03-11 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_version'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='version',
            options={'verbose_name': 'Версия', 'verbose_name_plural': 'Версии'},
        ),
        migrations.AlterField(
            model_name='version',
            name='number',
            field=models.FloatField(help_text='Укажите номер версии', verbose_name='Номер версии'),
        ),
        migrations.AlterField(
            model_name='version',
            name='working_ver',
            field=models.BooleanField(help_text='Укажите признак текущей версии', verbose_name='Признак версии'),
        ),
    ]

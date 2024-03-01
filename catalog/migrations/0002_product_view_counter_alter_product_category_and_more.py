# Generated by Django 5.0.2 on 2024-02-29 14:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='view_counter',
            field=models.PositiveIntegerField(default=0, help_text='Укажите кол-во просмотров', verbose_name='Счетчик просмотров'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, help_text='Категория товара', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='catalog.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, help_text='Опишите товар', null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, help_text='Фото товара', null=True, upload_to='prod_images', verbose_name='Изображение (превью)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(help_text='Укажите наименование товара', max_length=50, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(help_text='Стоимость товара', verbose_name='Цена за покупку'),
        ),
    ]
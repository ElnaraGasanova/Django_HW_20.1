# Generated by Django 5.0.2 on 2024-03-01 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_product_view_counter_alter_product_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Укажите заголовок', max_length=100, verbose_name='Заголовок')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Slug')),
                ('content', models.TextField(blank=True, help_text='Добавьте описание', null=True, verbose_name='Содержимое')),
                ('image', models.ImageField(blank=True, help_text='Приложите фото', null=True, upload_to='blog_images', verbose_name='Изображение (превью)')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('published', models.BooleanField(default=False, verbose_name='Опубликовано')),
                ('view_counter', models.PositiveIntegerField(default=0, help_text='Укажите кол-во просмотров', verbose_name='Счетчик просмотров')),
            ],
            options={
                'verbose_name': 'Публикация',
                'verbose_name_plural': 'Публикации',
                'ordering': ['created_at', 'published', 'view_counter'],
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='view_counter',
        ),
    ]

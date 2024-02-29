from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name',]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование', help_text='Укажите наименование товара')
    description = models.TextField(verbose_name='Описание', **NULLABLE, help_text='Опишите товар')
    image = models.ImageField(upload_to='prod_images', verbose_name='Изображение (превью)',
                              **NULLABLE, help_text='Фото товара')
    category = models.ForeignKey('Category', related_name='products', verbose_name='Категория',
                                 on_delete=models.SET_NULL, **NULLABLE, help_text='Категория товара')
    price = models.IntegerField(verbose_name='Цена за покупку', help_text='Стоимость товара')
    created_at = models.DateField(verbose_name='Дата создания (записи в БД)', auto_now_add=True, **NULLABLE)
    updated_at = models.DateField(verbose_name='Дата последнего изменения (записи в БД)', auto_now=True, **NULLABLE)
    #manufactured_at = models.DateField(verbose_name='Дата производства продукта', auto_now=True, **NULLABLE)
    view_counter = models.PositiveIntegerField(verbose_name='Счетчик просмотров',
                                               help_text='Укажите кол-во просмотров', default=0)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name",]

    def __str__(self):
        return f' {self.name}'

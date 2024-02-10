from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='images/products/', verbose_name='Изображение (превью)', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    created_at = models.DateTimeField(verbose_name='Дата создания (записи в БД)', auto_now_add=True, **NULLABLE)
    updated_at = models.DateTimeField(verbose_name='Дата последнего изменения (записи в БД)', auto_now=True, **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} цена: {self.price}, категория: {self.category}'

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукт"
        ordering = ("name",)


categ_1 = Category.objects.create(name='Овощи и Фрукты')
categ_2 = Category.objects.create(name='Бакалея')
categ_3 = Category.objects.create(name='Хозтовары')
categ_4 = Category.objects.create(name='Одежда')
prduct_1 = Product.objects.create(name='Ананас', category=categ_1)
prduct_2 = Product.objects.create(name='Кофе', category=categ_2)
prduct_3 = Product.objects.create(name='Пакеты для мусора', category=categ_3)
prduct_4 = Product.objects.create(name='Пижама', category=categ_4)

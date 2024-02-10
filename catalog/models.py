from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


categ_1 = Category.objects.create(name='Овощи и Фрукты')
categ_2 = Category.objects.create(name='Бакалея')
categ_3 = Category.objects.create(name='Хозтовары')
categ_4 = Category.objects.create(name='Одежда')
prduct_1 = Product.objects.create(name='Ананас', category=categ_1)
prduct_2 = Product.objects.create(name='Кофе', category=categ_2)
prduct_3 = Product.objects.create(name='Пакеты для мусора', category=categ_3)
prduct_4 = Product.objects.create(name='Пижама', category=categ_4)

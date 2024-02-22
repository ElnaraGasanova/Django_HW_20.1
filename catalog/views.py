from django.shortcuts import render
from catalog.models import Product

def home(request):
    '''Выводит на страницы трех питомцев'''
    products = Product.objects.all()
    context = {
        'object_list': products
    }
    return render(request, 'catalog/home.html', context)

def contacts(request):
    return render(request, 'catalog/contacts.html')


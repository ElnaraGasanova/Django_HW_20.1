from django.shortcuts import render, get_object_or_404
from catalog.models import Product

def home(request):
    '''Выводит на страницу все товары'''
    products = Product.objects.all()
    context = {
        'object_list': products
    }
    return render(request, 'catalog/home.html', context)

def product_info(request, pk):
    '''Выводит на страницу товар по pk.'''
    product = get_object_or_404(Product, pk=pk)
    context = {
        'object': product
    }
    return render(request, 'dogs/product_info.html', context)


# def contacts(request):
#     return render(request, 'catalog/contacts.html')


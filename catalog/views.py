from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from catalog.models import Product


# Контроллер CBV
class HomeView(ListView):
    model = Product

# Контроллер CBV
class ProductDetailView(DetailView):
    model = Product


# Контроллер FBV
def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    context = {
        'title': 'contact'
    }
    return render(request, 'catalog/contacts.html', context)

# Контроллер FBV
# def home(request):
#     '''Выводит на страницу все товары'''
#     products = Product.objects.all()
#     context = {
#         'object_list': products
#     }
#     return render(request, 'catalog/product_list.html', context)


# Контроллер FBV
# def product_info(request, pk):
#     '''Выводит на страницу товар по pk.'''
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         'object': product
#     }
#     return render(request, 'catalog/product_detail.html', context)

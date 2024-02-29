from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product


# Контроллер CBV
class HomeView(ListView):
    model = Product

# Контроллер CBV
class ProductDetailView(DetailView):
    model = Product


# Контроллер CBV
# class ContactsPageView(TemplateView):
#     template_name = "contacts.html"

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


class ProductCreateView(CreateView):
    '''Описываем поля, которые будут заполняться при создании нового продукта'''
    model = Product
    fields = ('name', 'price', 'image')
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    '''Описываем поля, которые будут заполняться при изменении данных продукта'''
    model = Product
    fields = ('name', 'price', 'image', 'category')

    def get_success_url(self):
        return reverse_lazy('catalog:product_info', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')

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

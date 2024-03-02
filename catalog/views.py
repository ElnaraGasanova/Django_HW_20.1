from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product, Blog


# Контроллер CBV
class HomeView(ListView):
    model = Product


# Контроллер CBV
class ProductDetailView(DetailView):
    model = Product

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     self.object.view_counter += 1
    #     self.object.save()
    #     return self.object


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


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    '''Описываем поля, которые будут заполняться при создании нов.публикации'''
    model = Blog
    fields = ('title', 'content', 'image')
    success_url = reverse_lazy('catalog:blg')


class BlogUpdateView(UpdateView):
    '''Описываем поля, которые будут заполняться при изменении данных публикации'''
    model = Blog
    fields = ('title', 'content', 'image', 'published')

    def get_success_url(self):
        return reverse_lazy('catalog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blg')

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


# Контроллер CBV
# class ContactsPageView(TemplateView):
#     template_name = "contacts.html"
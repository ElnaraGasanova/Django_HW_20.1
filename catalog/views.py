from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Product, Blog


# Контроллер CBV
class HomeView(ListView):
    model = Product

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        return queryset


# Контроллер CBV
class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.save()
        return self.object


class ProductCreateView(CreateView):
    '''Описываем поля, которые будут заполняться при создании нов.продукта'''
    model = Product
    fields = ('name', 'description', 'price', 'image',)
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    '''Описываем поля, которые будут заполняться при изменении данных продукта'''
    model = Product
    fields = ('name', 'description', 'price',)

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('catalog:product_detail', args=[self.kwargs.get('pk')])

    # def form_valid(self, form):
    #     if form.is_valid():
    #         new_blog = form.save()
    #         new_blog.slug = slugify(new_blog.title)
    #         new_blog.save()
    #
    #     return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')


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

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


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
    fields = ('title', 'content', 'image', 'is_published')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('catalog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blg')


def toggle_published(request, pk):
    publication_item = get_object_or_404(Blog, pk=pk)
    if publication_item.is_published:
        publication_item.is_published = False
    else:
        publication_item.is_published = True

    publication_item.save()

    return redirect(reverse_lazy('catalog:blg'))

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
from django.urls import path
from catalog.views import HomeView, ProductDetailView, contacts, BlogCreateView, BlogUpdateView, BlogDeleteView
from django.conf.urls.static import static
from django.conf import settings
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_info'),
    path('contacts/', contacts, name='w'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#     path('contacts/', ContactsPageView.as_view(), name='w')
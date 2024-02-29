from django.urls import path
from catalog.views import HomeView, ProductDetailView, contacts
from django.conf.urls.static import static
from django.conf import settings
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_info'),
    path('contacts/', contacts, name='w')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
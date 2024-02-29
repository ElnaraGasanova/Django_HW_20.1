from django.urls import path
from catalog.views import HomeView, ProductDetailView, contacts, ProductCreateView, ProductUpdateView, ProductDeleteView
from django.conf.urls.static import static
from django.conf import settings
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_info'),
    path('contacts/', contacts, name='w'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#     path('contacts/', ContactsPageView.as_view(), name='w')
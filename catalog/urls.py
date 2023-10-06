from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import contact, IndexView, ProductDetailView, ProductCreateView, ProductListView, ProductUpdateView, \
    ProductDeleteView, VersionCreateView, VersionUpdateView, VersionDeleteView, categories

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', contact, name='contact'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('create/', never_cache(ProductCreateView.as_view()), name='product_create'),
    path('list/', ProductListView.as_view(), name='list_product'),
    path('edit_product/<int:pk>', never_cache(ProductUpdateView.as_view()), name='edit_product'),
    path('delete_product/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
    path('product/<int:pk>/create_version/', VersionCreateView.as_view(), name='version_create'),
    path('edit_version/<int:pk>', VersionUpdateView.as_view(), name='edit_version'),
    path('delete_version/<int:pk>', VersionDeleteView.as_view(), name='delete_version'),
    path('categories', categories, name='categories'),

]

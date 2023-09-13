from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contact, get_product, IndexView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', contact, name='contact'),
    path('product/<pk>/', get_product),
]

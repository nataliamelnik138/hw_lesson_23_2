from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contact, IndexView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', contact, name='contact'),
    path('product/<int:pk>/', ProductDetailView.as_view()),
]

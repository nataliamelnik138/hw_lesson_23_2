from django.urls import path

from catalog.views import index, contact

app_name = 'catalog'

urlpatterns = [
    path('', index),
    path('contacts/', contact)
]

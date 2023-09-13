from django.shortcuts import render
from django.views.generic import TemplateView

from catalog.models import Product


class IndexView(TemplateView):
    template_name = 'catalog/index.html'
    extra_context = {
        'title': 'Главная страница'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.all()[:5]
        return context_data


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contact.html', context)


def get_product(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'title': product.product_name,
        'product': product

    }
    print(context['product'])
    return render(request, f'catalog/product.html', context=context)

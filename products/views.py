from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'Store'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Каталог продукции'
    }
    return render(request, 'products/products.html', context)


def test_context(request):
    context = {
        'title': 'Store',
        'header': 'Добро пожаловать!',
        'username': 'Иван Иванов',
    }
    return render(request, 'products/test-context.html', context)
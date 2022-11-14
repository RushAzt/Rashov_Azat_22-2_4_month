from django.shortcuts import render
from products.models import Product
# Create your views here.

def product_detail_view(request, id):
    dict_ = {}
    product = Product.objects.get(id=id)
    dict_['product_detail'] = product
    return render(request, 'detail.html', context=dict_)

def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/main.html')

def product_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        data = {
            'products': products
        }

        return render(request, 'products/products.html', context=data)

def categories_view(request):
    if request.method == 'GET':
        return render(request, 'categories/categories.html')


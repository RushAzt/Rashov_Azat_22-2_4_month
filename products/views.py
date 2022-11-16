from django.shortcuts import render
from products.models import Product, Comment
# Create your views here.


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/main.html')
def product_detail_view(request, id):
    if request.method == "GET":
        product = Product.objects.get(id=id)
        comments = Comment.objects.filter(product_id=id)
        data = {
            'product': product,
            'comments': comments
        }
    return render(request, 'products/detail.html', context=data)
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


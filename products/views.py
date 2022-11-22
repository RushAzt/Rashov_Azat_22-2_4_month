from django.shortcuts import render
from products.models import Product, Comment, Category
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
        category_id = request.GET.get('category_id')

        if category_id:
            products = Product.objects.filter(categories__in=[category_id])
        else:
            products = Product.objects.all()

        products = [{
            'id': product.id,
            'title': product.title,
            'image': product.image,
            'description': product.description,
            'price': product.price,
            'amount': product.amount,
            'categories': product.categories
        } for product in products]

        data = {
            'products': products
        }

        return render(request, 'products/products.html', context=data)


def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        data = {
            'categories': categories
        }
        return render(request, 'categories/categories.html', context=data)


from django.shortcuts import render, redirect
from products.models import Product, Comment, Category
from .forms import ProductCreateForm, ReviewCreateForm



def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/main.html')
def product_detail_view(request, id):
    if request.method == "GET":
        product = Product.objects.get(id=id)
        comments = Comment.objects.filter(product_id=id)
        data = {
            'product': product,
            'comments': comments,
            'form': ReviewCreateForm
        }
        return render(request, 'products/detail.html', context=data)
    if request.method == "POST":
        form = ReviewCreateForm(data=request.POST)

        if form.is_valid():
            Comment.objects.create(
                author_id=1,
                text=form.cleaned_data.get('text'),
                product_id=id
            )
            return redirect(f'/product/{id}/')
        else:
            product = Product.objects.get(id=id)
            comments = Comment.objects.filter(product_id=id)
            data = {
                'product': product,
                'comments': comments,
                'form': form
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


def product_create_view(request):
    if request.method == "GET":
        data = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=data)
    if request.method == "POST":
        form = ProductCreateForm(data=request.POST)

        if form.is_valid():
            Product.objects.create(
                author_id=1,
                # image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price'),
                amount=form.cleaned_data.get('amount'),
                # categories=
            )
            return redirect('/product')
        else:
            data = {
                'form': form
            }
            return render(request, 'products/create.html', context=data)
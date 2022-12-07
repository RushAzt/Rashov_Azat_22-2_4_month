from django.shortcuts import render, redirect
from products.models import Product, Comment, Category
from .forms import ProductCreateForm, ReviewCreateForm
from users.utils import get_user_from_request
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView


class MainView(ListView):
    model = Product
    template_name = 'layouts/main.html'
    context_object_name = "product"
class DetailProductView(CreateView, DetailView):
    template_name = 'products/detail.html'
    form_class = ReviewCreateForm
    model = Product
    pk_url_kwarg = 'id'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'user': get_user_from_request(self.request),
            'form': kwargs['form'] if kwargs.get('form') else self.form_class,
            'product': self.get_object(),
            'comment': kwargs['comment'],
        }

    def product(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            Comment.objects.create(
                author_id=request.user.id,
                text=form.cleaned_data.get('text'),
                product_id=kwargs['id'],
            )
            return redirect(f'/product/{kwargs["id"]}/')
        else:
            product = Product.objects.get(id=kwargs["id"])
            comment = Comment.objects.filter(product_id=kwargs["id"])
            categories = product.category.all()

            return render(request, self.template_name, context=self.get_context_data(
                form=form,
                product=product,
                comment=comment,
                categories=categories
            ))

    def get(self, request, *args, **kwargs):

        product = Product.objects.get(id=kwargs["id"])
        comment = Comment.objects.filter(product_id=kwargs["id"])

        return render(request, self.template_name, context=self.get_context_data(
            product=product,
            comment=comment,
        ))



PAGINATION_LIMIT = 3

class ProductView(ListView):
    model = Product
    template_name = 'products/products.html'

    def get_context_data(self, **kwargs):
        return {
            'products': kwargs['products'],
            'user': get_user_from_request(self.request),
            'max_page': range(1, kwargs['max_page'] + 1)
        }

    def get(self, request, *args, **kwargs):
        category_id = request.GET.get('category_id')
        search_word = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if category_id:
            products = Product.objects.filter(categories__in=[category_id])
        else:
            products = Product.objects.all()
        if search_word:
            products = products.filter(title__icontains=search_word)
        products = [{
            'id': product.id,
            'title': product.title,
            'image': product.image,
            'description': product.description,
            'price': product.price,
            'amount': product.amount,
            'categories': product.categories
        } for product in products]

        max_page = round(products.__len__() / PAGINATION_LIMIT)
        products = products[PAGINATION_LIMIT * (page - 1): PAGINATION_LIMIT * page]

        return render(request, self.template_name, context=self.get_context_data(
            products=products,
            max_page=max_page
        ))



class CategoriesView(ListView):
    model = Category
    template_name = 'categories/categories.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
        'categories': self.get_queryset(),
        'user': get_user_from_request(self.request)
        }


class ProductCreateView(ListView, CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'products/create.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'user': get_user_from_request(self.request),
            'form': kwargs['form'] if kwargs.get('form') else self.form_class
        }

    def product(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            self.model.objects.create(
                author_id=request.user.id,
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price'),
            )
            return redirect('/product')
        else:
            return render(request, self.template_name, context=self.get_context_data(form=form))
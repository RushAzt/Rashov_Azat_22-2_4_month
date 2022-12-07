from django.urls import path
from products.views import ProductView, CategoriesView, ProductCreateView, DetailProductView, MainView

urlpatterns = [
    path('product/', ProductView.as_view()),
    path('categories/', CategoriesView.as_view()),
    path('online-store/', MainView.as_view()),
    path('product/<int:id>/', DetailProductView.as_view()),
    path('product/create/', ProductCreateView.as_view()),

]



from django.urls import path
from products.views import product_view, categories_view, main_view, product_detail_view, product_create_view

urlpatterns = [
    path('product/', product_view),
    path('categories/', categories_view),
    path('online-store/', main_view),
    path('product/<int:id>/', product_detail_view),
    path('product/create/', product_create_view),

]



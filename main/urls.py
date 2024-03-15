from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('search',search,name='search'),
    path('category-list', category_list,name='category-list'),
    path('brand-list', brand_list,name='brand-list'),
    path('product-list', product_list,name='product-list'),
    path('category-product-list/<int:cat_id>', category_product_list,name='category-product-list'),
    path('brand-product-list/<int:brand_id>', brand_product_list,name='brand-product-list'),
    path('product/<str:slug>/<int:id>',product_detail,name='product_detail'),
    path('filter-data',filter_data,name='filter_data'),
]
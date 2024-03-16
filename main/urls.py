from django.urls import path, include
from .views import *
from django.contrib.auth import views

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
    path('load-more-data',load_more_data,name='load_more_data'),
    path('add-to-cart',add_to_cart,name='add_to_cart'),
    path('cart',cart_list,name='cart'),
    path('delete-from-cart',delete_cart_item,name='delete-from-cart'),
    path('update-cart',update_cart_item,name='update-cart'),
    path('accounts/signup',signup,name='signup'),
    path('logout', logoutfunction, name='logout'),
    path('login/', views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('checkout', checkout,name='checkout'),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment-done/', payment_done, name='payment_done'),
    path('payment-cancelled/', payment_canceled, name='payment_cancelled'),
    path('save-review/<int:pid>',save_review, name='save-review'),
    path('my-dashboard',my_dashboard, name='my_dashboard'),
    path('my-orders',my_orders, name='my_orders'),
    path('my-orders-items/<int:id>',my_order_items, name='my_order_items'),
    path('add-wishlist',add_wishlist, name='add_wishlist'),
    path('my-wishlist',my_wishlist, name='my_wishlist'),
    path('my-reviews',my_reviews, name='my-reviews'),



]
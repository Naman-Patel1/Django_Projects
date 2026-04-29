from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='store-home'),
    path('products/', views.product_list, name='store-products'),
    path('product/<int:pk>/', views.product_detail, name='store-product-detail'),
    
    path('cart/', views.view_cart, name='store-cart'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='store-add-to-cart'),
    path('clear-cart/', views.clear_cart, name='store-clear-cart'),
    path('checkout/', views.checkout, name='store-checkout'),
    
    path('register/', views.register_view, name='store-register'),
    path('login/', views.login_view, name='store-login'),
    path('logout/', views.logout_view, name='store-logout'),
]

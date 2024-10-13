from django.urls import path
from . import views

urlpatterns = [

    path('search', views.search, name = 'search'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.general_home, name='gen_home'),
     path('category/', views.category_home, name='catagory_home'), 
    path('cart/', views.cart_view, name='cart_view'),
    path('cart/update/<int:product_id>/', views.update_cart, name='update_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('category/<int:pk>/', views.category_product, name='category_product'),  # Filtered category view
    path('product/<int:pk>/', views.product_details, name='product_detail'),  # Product details view
]

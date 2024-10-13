from django.contrib.auth import views as auth_views
from django.urls import path
from .views import About_as, vendor_detial,my_store, delete_product,SignUp, My_Account, addproduct, update_product,product_order_detail, my_orders

urlpatterns = [
    path('signup/', SignUp, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='Loginpage.html'), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path('myaccount/', My_Account, name='myaccount'),
    path('my_store/', my_store, name='my_store'), 
    path('my_store/my_orders/', my_orders, name='my_orders'), 
    path('my_store/my_orders/product_order_detail/<int:order_item_id>/', product_order_detail, name='product_order_detail'),
    
    path('vendors/<int:pk>/', vendor_detial, name='vendors'),  
    path('addproduct/', addproduct, name='add_product'),
    path('my-store/product-update/<int:pk>/', update_product, name='product_update'),
    path('my-store/delete-product/<int:pk>/', delete_product, name='delete_product'),
    path('about/', About_as, name='about'),
]

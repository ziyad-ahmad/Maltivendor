from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404 
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

from Stores.form import ProductForm
from Stores.models import Products, ProductReview , Order, OrderItem

@login_required
def My_Account(request):
    return render(request,"myAccount.html")

@login_required
def my_store(request):
    products = Products.objects.filter(added_by=request.user).exclude(status='DELETE') 
    return render(request, "my_store.html", {
        'products': products,
    })
@login_required
def my_orders(request):
    # Retrieve all order items for products added by the logged-in user
    order_items = OrderItem.objects.filter(product__added_by=request.user).select_related('')
    return render(request, 'my_orders.html', {
        'order_items': order_items,
    })

@login_required
def product_order_detail(request, order_item_id):
    # Retrieve a specific order item by its ID, ensuring it belongs to a product added by the user
    order_item = get_object_or_404(OrderItem, id=order_item_id, product__added_by=request.user)
    
    order = order_item.order  # This will fetch the associated order

    order_details = {
        'first_name': order.first_name,
        'last_name': order.last_name,
        'city': order.city,
        'address': order.address,
        'email': order.email,
        'postal_code': order.posta_code,
        'merchant_id': order.marchent_id,
        'paid_amount': order.paid_amount,
        'is_paid': order.is_paid,
        'status': order.get_status_display(),
        'created_at': order.created_at,
    }

    return render(request, 'detail_order.html', {
        'order_item': order_item,
        'order': order_details,  # Pass the detailed order information
    })
@login_required
def addproduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.added_by = request.user  # Automatically set the authenticated user
            product.save()
            return redirect('my_store')
    else:
        form = ProductForm()
    
    return render(request, 'add_product.html', {
        'form': form
    })

@login_required
def update_product(request, pk):
    product = get_object_or_404(Products, pk=pk)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "You are update the Product.")
            return redirect('my_store')  # Redirect to the user's store or another page
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'product_update.html', {'form': form, 'product': product})


@login_required
def delete_product(request, pk):
    product = get_object_or_404(Products, pk=pk, added_by=request.user)
    product.status = 'DELETE'
    product.save()

    messages.success(request, "Product successfully marked as deleted.")
    return redirect('my_store')

def SignUp(request):
    # Check if the request method is POST to handle form submission
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            UserProfile.objects.create(user=user)
            # Redirect to the login page or another desired page
            return redirect(reverse('login'))
    else:
        form = UserCreationForm()

    # Render the signup page with the form
    return render(request, 'signup.html', {'form': form})

def About_as(request):
    return render(request, 'about.html')

def vendor_detial(request, pk):
    users = User.objects.get(pk= pk)
    products =  Products.objects.filter(status= Products.ACTIVE)
    return render(request, 'verdor_detail.html',{
        'users':users,
        'products':products
    })
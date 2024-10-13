from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Products, Categories, Order, OrderItem
from django.contrib import messages
from .cart import Cart
from .form import OrederForm

def general_home(request):
    products = Products.objects.filter(status=Products.ACTIVE).order_by('-created_at')[:5]
    return render(request, 'genHome.html', {'products': products})

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id=product_id, quantity=1)
    messages.success(request, 'Product added to cart!')
    return redirect('catagory_home')  # Change this to the appropriate URL name for your home view

def cart_view(request):
    cart = Cart(request)  # Initialize the cart
    
    # Get cart items using the get_items method
    items = cart.get_items()
    
    # Calculate the total price
    subtotal = cart.get_total_price()
    shipping_estimate = 5.00  # Static value for shipping
    tax_estimate = 8.32  # Static value for tax
    order_total = subtotal + shipping_estimate + tax_estimate

    context = {
        'cart': cart,
        'items': items,  # Pass the list of items to the template
        'subtotal': subtotal,
        'shipping_estimate': shipping_estimate,
        'tax_estimate': tax_estimate,
        'order_total': order_total,
    }
    return render(request, 'cart_vew.html', context) 


def update_cart(request, product_id):
  
    cart = Cart(request)
    action = request.POST.get('action')
    current_quantity = cart.get_item_quantity(product_id)

    if action == 'increment':
        new_quantity = current_quantity + 1
    elif action == 'decrement':
        new_quantity = max(current_quantity - 1, 1)  
    else:
        # Default case, if no valid action is provided
        new_quantity = current_quantity

    # Update the quantity in the cart
    cart.add(product_id=product_id, quantity=new_quantity, update_quantity=True)
    messages.success(request, 'Cart updated successfully!')

    return redirect('cart_view')

def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id=product_id)
    messages.success(request, 'Product removed from cart.')
    return redirect('cart_view')  # Ensure this matches the URL name of your cart view

def checkout(request):
    cart = Cart(request)

    # Initialize the form outside the `POST` check
    form = OrederForm()

    if request.method == 'POST':
        form = OrederForm(request.POST)  # Use POST data to create the form instance
        if form.is_valid():
            total_price = 0 
            for item in cart.get_items():  # Use cart.get_items() to iterate through the items
                product = item['product']
                total_price += product.initial_sell * int(item['quantity'])

            # Create the order but don't save it yet
            order = form.save(commit=False)
            order.created_by = request.user
            order.paid_amount = total_price
            order.save()

            # Create order items
            for item in cart.get_items():
                product = item['product']
                quantity = int(item['quantity'])  # Fix incorrect function call
                price = product.initial_sell * quantity
                OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)

            # Clear the cart after successful order creation
            cart.clear()

            # Show success message and redirect to 'myaccount'
            messages.success(request, "Your order has been placed successfully!")
            return redirect('myaccount')
        else:
            # If the form is not valid, display an error message
            messages.error(request, "There was an issue with your order. Please try again.")

    return render(request, 'checkout.html', {
        'cart': cart,
        'form': form  # Ensure form is always defined
    })  # Change this to your order confirmation URL


def search(request):
    query = request.GET.get('query', '')  # Get the search query
    products = []
    if query.strip():  # Ensure the query is not empty
        products = Products.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'search.html', {'products': products, 'query': query})

def category_home(request):
    categories = Categories.objects.all()  # Fetch all categories
    products = Products.objects.filter().exclude(status='DELETE') # Fetch all products (initial view without filtering)
    
    context = {
        'categories': categories,  # Send categories for sidebar
        'products': products  # Send all products to display in the body
    }
    return render(request, 'Home.html', context)  # Use 'home.html' as the main template

# View to display products based on selected category
def category_product(request, pk):
    categories = Categories.objects.all()  # Fetch all categories for sidebar
    category = get_object_or_404(Categories, pk=pk)  # Get selected category
    products = Products.objects.filter(category=category, status=Products.ACTIVE)  # Fetch products under this category
    
    context = {
        'categories': categories,  # Send categories for sidebar
        'selected_category': category,  # Highlight the selected category
        'products': products  # Send filtered products to display in the body
    }
    return render(request, 'home.html', context)  # Render the same template for consistency

# Product details view
def product_details(request, pk):
    product = get_object_or_404(Products, pk=pk)
    
    context = {
        "product": product
    }
    return render(request, 'product_detail.html', context)
 
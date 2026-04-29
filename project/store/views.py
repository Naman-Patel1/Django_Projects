from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product

def home(request):
    products = Product.objects.all().order_by('-created_at')[:3]
    return render(request, 'store/index.html', {'products': products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/products.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == "POST":
        cart = request.session.get('cart', {})
        str_pk = str(pk)
        
        if str_pk in cart:
            cart[str_pk]['quantity'] += 1
        else:
            cart[str_pk] = {
                'name': product.name,
                'price': float(product.price),
                'quantity': 1,
            }
            if product.image:
                cart[str_pk]['image'] = product.image.url
            elif product.image_url:
                cart[str_pk]['image'] = product.image_url
            else:
                cart[str_pk]['image'] = ''
                
        request.session['cart'] = cart
        messages.success(request, f"{product.name} was added to your cart.")
        
    return redirect('store-products')

def view_cart(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'store/cart.html', {'cart': cart, 'total': total})

def clear_cart(request):
    if 'cart' in request.session:
        del request.session['cart']
        messages.success(request, "Cart cleared successfully!")
    return redirect('store-cart')

def checkout(request):
    if 'cart' in request.session:
        cart = request.session['cart']
        total = sum(item['price'] * item['quantity'] for item in cart.values())
        order_date = timezone.now()
        
        bill_data = {'cart': dict(cart), 'total': total, 'date': order_date}
        
        del request.session['cart']
        messages.success(request, "Order placed successfully! Here is your bill.")
        return render(request, 'store/bill.html', bill_data)
    else:
        messages.warning(request, "Your cart is empty.")
    return redirect('store-home')

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("store-home")
    else:
        form = UserCreationForm()
    return render(request, 'store/register.html', {"register_form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("store-home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'store/login.html', {"login_form": form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("store-home")

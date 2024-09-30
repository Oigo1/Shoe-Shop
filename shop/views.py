from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect
from .models import Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect

# Create your views here.

def home(request):
    products = Product.objects.all() #Fetches all products from the database
    return render(request, 'shop/home.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    sizes = range(39, 47)  # This will generate sizes from 39 to 46.
    return render(request, 'shop/product_detail.html', {'product': product, 'sizes': sizes})

def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    subtotal = 0

    for product_id, details in cart.items():
        product = Product.objects.get(id=product_id)
        quantity = details['quantity']
        size = details['size']
        total_price = product.price * quantity
        subtotal += total_price

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'size': size,
            'total_price': total_price
        })
    
    shipping = 10 # Example fixed shipping cost
    total = subtotal + shipping

    return render(request, 'shop/cart.html', {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'shipping': shipping,
        'total': total
    })


@csrf_protect
def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        size = request.POST.get('size')  # Get the selected size from the form
        quantity = int(request.POST.get('quantity', 1))  # Default quantity to 1

        cart = request.session.get('cart', {})

        if str(product_id) in cart:
            cart[str(product_id)]['quantity'] += quantity
        else:
            cart[str(product_id)] = {'quantity': quantity, 'size': size}

        request.session['cart'] = cart

        # Calculate the total number of items in the cart
        cart_count = sum(item['quantity'] for item in cart.values())

        # Update the session with the cart count
        request.session['cart_count'] = cart_count

        # If it's an AJAX request, return JSON response with the cart count
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                'cart_count': cart_count,
                'message': 'Item successfully added to cart!'
            })
        else:
            return redirect('cart')  # If it's not an AJAX request, fallback to redirecting


def cart_update(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        action = request.POST.get('action')

        # Get the cart and item from the session
        cart = request.session.get('cart', {})
        item = cart.get(product_id)

        if item:
            if action == 'increase':
                item['quantity'] += 1
            elif action == 'decrease' and item['quantity'] > 1:
                item['quantity'] -= 1
            # save back to session 
            request.session['cart'] = cart
        return JsonResponse({'status': 'success'})
    
    return JsonResponse({'status': 'error'}, status=400)


def cart_delete(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')

        # Get the cart from the session
        cart = request.session.get('cart', {})

        # Remove the product from the cart 
        if product_id in cart:
            del cart[product_id]
            request.session['cart'] = cart

        return JsonResponse({'status': 'success'})
    
    return JsonResponse({ 'status': 'error' }, status=400)
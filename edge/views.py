from django.shortcuts import render
from .models import Flower

from django.shortcuts import HttpResponse
from django.views.decorators.http import require_POST
import json
from django.http import JsonResponse
from django.shortcuts import redirect


# Create your views here.
def index(request):
    flowers = Flower.objects.all()
    for flower in flowers:
        print(flower.image)
    return render(request, 'edge/index.html', {'flowers': flowers})

def flowers(request):
    flowers = Flower.objects.all()
    for flower in flowers:
        print(flower.image)
    return render(request, 'edge/Flowers.html', {'flowers': flowers})

def aboutus(request):
    return render(request, 'edge/aboutus.html')

def contact(request):
    return render(request, 'edge/contactus.html')

def delivery(request):
    return render(request, "edge/Delivery.html")

def wishlist(request):
    return render(request, 'edge/wishlist.html')

def products(request, id):
    flower = Flower.objects.get(pk=id)
    return render(request, "edge/products.html", {'flower':  flower})

def add_to_cart(request):
    if request.method == 'POST':
        flower_id = request.POST.get('flower_id')
        flower_size = request.POST.get('flower_size')
        print(flower_size)
        cart = request.session.get('cart', [])

        cart.append(flower_id + ',' + flower_size)

        request.session['cart'] = cart
        return HttpResponse(json.dumps({'success': True}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({'error': 'Method not allowed'}), status=405, content_type="application/json")

def remove_from_cart(request):
    if request.method == 'POST':
        # Assuming the product ID is sent in the request body
        data = json.loads(request.body)
        flower_id = data.get('flower_id')
        flower_size = data.get('flower_size')
        flower = (str(flower_id) + ',' + flower_size)

        # Remove the product from the session
        if 'cart' in request.session:
            cart = request.session['cart']
            if flower in cart:
                cart.remove(flower)
                request.session['cart'] = cart
                print(cart)
                return JsonResponse({'message': 'Product removed from cart'}, status=200)
            else:
                return JsonResponse({'error': 'Product not found in cart'}, status=400)
        else:
            return JsonResponse({'error': 'Cart not found in session'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)

def get_cart(request):
    cart = request.session.get('cart', [])
    # You may want to retrieve the actual product objects based on the product IDs in the cart
    # For simplicity, I'll just return the product IDs as JSON
    print(cart)
    cart_html = ''
    cart_total_price = 0
    if cart:
        for flower in cart:
            cart_html += '<div class="checkoutlist">'
            flower = flower.split(',')
            flower_id = flower[0]
            flower_size = flower[1]
            flower = Flower.objects.get(pk=flower_id)
            cart_html += '<div class = "checkoutimage"><img src="/edge/media/{0}" alt="" /></div>'.format(flower.image)
            cart_html += '<div class="checkdetail"> <div class="checkfirst">'
            cart_html += '<h2>{0}</h2>'.format(flower.name)
            cart_html += '<svg  onclick="removeCart({0},\'{1}\')" fill="#B7B0B5" height="clamp(1rem, 1.5vw, 2rem)" viewBox="0 0 32 32" version="1.1" xmlns="http://www.w3.org/2000/svg"> <path d="M16 0c-8.836 0-16 7.163-16 16s7.163 16 16 16c8.837 0 16-7.163 16-16s-7.163-16-16-16zM16 30.032c-7.72 0-14-6.312-14-14.032s6.28-14 14-14 14 6.28 14 14-6.28 14.032-14 14.032zM21.657 10.344c-0.39-0.39-1.023-0.39-1.414 0l-4.242 4.242-4.242-4.242c-0.39-0.39-1.024-0.39-1.415 0s-0.39 1.024 0 1.414l4.242 4.242-4.242 4.242c-0.39 0.39-0.39 1.024 0 1.414s1.024 0.39 1.415 0l4.242-4.242 4.242 4.242c0.39 0.39 1.023 0.39 1.414 0s0.39-1.024 0-1.414l-4.242-4.242 4.242-4.242c0.391-0.391 0.391-1.024 0-1.414z"></path> </svg>'.format(flower_id, flower_size)
            cart_html += '</div> <div class="checksecond"><h2>Size:</h2>'
            cart_html += '<h2>{0}</h2></div><div class="row2"><button class="minus" id="{1}" onclick="sub(this.id)">&#8210;</button><input id="input_{1}" type="text" value=1 /><button class="plus" id="{1}" onclick="add(this.id)">&plus;</button></div>'.format(flower_size, flower_id)
            cart_html += '</div></div>'
            if flower_size == 'S':
                flower_price = flower.price_s
            elif flower_size == 'M':
                flower_price = flower.price_m
            elif flower_size == 'L':
                flower_price = flower.price_l
            elif flower_size == 'XL':
                flower_price = flower.price_xl
            elif flower_size == 'XXL':
                flower_price = flower.price_xxl
            cart_total_price += flower_price
    return JsonResponse({'html': cart_html, 'total_price': cart_total_price})

def checkout(request):
    cart = request.session.get('cart', [])
    # You may want to retrieve the actual product objects based on the product IDs in the cart
    # For simplicity, I'll just return the product IDs as JSON
    print(cart)
    cart_html = ''
    flowers = []
    flower_sizes = []
    flower_price = []
    if cart:
        for flower in cart:
            flower = flower.split(',')
            flower_id = flower[0]
            flower_size = flower[1]
            flower_sizes.append(flower_size)
            flower = Flower.objects.get(pk=flower_id)
            flowers.append(flower)
            if flower_size == 'S':
                flower_price.append(flower.price_s)
            elif flower_size == 'M':
                flower_price.append(flower.price_m)
            elif flower_size == 'L':
                flower_price.append(flower.price_l)
            elif flower_size == 'XL':
                flower_price.append(flower.price_xl)
            elif flower_size == 'XXL':
                flower_price.append(flower.price_xxl)
        total_price = 0
        for price in flower_price:
            total_price += price
        return render(request, "edge/checkout.html", {'flowers': flowers, 'flower_sizes': flower_sizes, 'flower_price': flower_price,'total_price': total_price})
    return redirect("edge/Flowers.html")
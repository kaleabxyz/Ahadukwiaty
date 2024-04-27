from django.shortcuts import render
from .models import Flower

# Create your views here.
def index(request):
    return render(request, 'edge/index.html')

def flowers(request):
    flowers = Flower.objects.all()
    return render(request, 'edge/Flowers.html', {'flowers': flowers})

def aboutus(request):
    return render(request, 'edge/aboutus.html')

def contact(request):
    return render(request, 'edge/contactus.html')

def delivery(request):
    return render(request, "edge/Delivery.html")

def wishlist(request):
    return render(request, 'edge/wishlist.html')

def products(request):
    return render(request, "edge/products.html")

def checkout(request):
    return render(request, "edge/checkout.html")
from django.urls import path
from . import views

urlpatterns = [
        path("", views.index, name="index"),
        path("aboutus/", views.aboutus, name='aboutus' ),
        path("contactus/", views.contact, name="contactus"),
        path("flower/", views.flowers, name="flower"),
        path("delivery/", views.delivery, name="delivery"),
        path("wishlist/", views.wishlist, name="wishlist"),
        path("products.html", views.products, name="products"),
]

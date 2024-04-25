from django.urls import path
from . import views

urlpatterns = [
        path("", views.index, name="home"),
        path("aboutus/", views.aboutus, name='aboutus' ),
        path("contactus/", views.contact, name="contactus"),
        path("flower/", views.flowers, name="flower"),
        path("delivery/", views.delivery, name="delivery"),
        path("wishlist/", views.wishlist, name="wishlist"),
        path("products/", views.products, name="products"),
        path("checkout/", views.checkout, name="checkout"),
]

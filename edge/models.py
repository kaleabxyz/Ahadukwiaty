from django.db import models

class Flower(models.Model):
    SIZE_CHOICES = [
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    size = models.CharField(max_length=3, choices=SIZE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Add price field
    image = models.ImageField(upload_to='edge/images/')  # Add image field

    def __str__(self):
        return self.name
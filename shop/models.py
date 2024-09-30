from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(default='No description available')
    image = models.ImageField(upload_to='product_images')
    image1 = models.ImageField(upload_to='product_images', blank=True, null=True)
    image2 = models.ImageField(upload_to='product_images', blank=True, null=True)
    image3 = models.ImageField(upload_to='product_images', blank=True, null=True)
    image4 = models.ImageField(upload_to='product_images', blank=True, null=True)

    def __str__(self):
        return self.name


from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

PRODUCT_CATOGERY = (
    ("phone",'phone'),
    ("computer",'computer'),
    ("smart_watch",'smart watch'),
    ("headphone",'headphone'),
    ("gaming",'gaming'),
    ("camera",'camera'),
)
PRODUCT_COLOR = (

)


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    price = models.IntegerField()
    product_category = models.CharField(max_length=255, choices=PRODUCT_CATOGERY)
    discription = models.TextField()
    date = models.DateField(default=datetime.now)
    discount = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    rating = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    no_of_people_rated = models.PositiveIntegerField()
    product_image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.product_name
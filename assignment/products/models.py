from django.db import models


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# ASSUMING INFINITE ITEMS AVAILABLE
# class Item(models.Model):
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)


# class Order(models.Model):
#   deal_id = 

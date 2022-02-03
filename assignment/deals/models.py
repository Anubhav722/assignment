from django.db import models

from products.models import Product

# Create your models here.


# Product

# Deal
# p1: item_quantity, p2: item_quantity2, p3: item_quantity3

# ProductDealRelation:
# deal_id = 



# 1 product


class Deal(models.Model):
    """
    can also be on a list or products
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    deal_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    start_time = models.DateTimeField('date added')
    end_time = models.DateTimeField('date ended')
    items = models.IntegerField(default=0)
    available_items = models.IntegerField(default=0)

    def __str__(self):
        return self.deal_name

from django.db import models

from deals.models import Deal

# Create your models here.


class Order(models.Model):
    """

    """
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE)
    user_id = models.IntegerField(default=0)

    def __str__(self):
        return self.deal.name + str(self.user_id)


# class OrderLog(models.Model):

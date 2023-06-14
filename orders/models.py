from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from products.models import Product


class SalesOrder(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    data = models.DateTimeField(default=timezone.now)
    customer_name = models.CharField(max_length=100, default='')
    is_paid = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    shipping_address = models.TextField(default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Product)
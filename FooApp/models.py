import uuid
from django.db import models


class Product(models.Model):
    prod_id = models.CharField(unique=True, default=uuid.uuid4, max_length=999)
    name = models.CharField(default="", max_length=300)
    description = models.TextField(default="Description here", max_length=999)
    price = models.DecimalField(max_digits=6, decimal_places=2)
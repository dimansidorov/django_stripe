from django.db import models
from django.core.validators import MinValueValidator


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.DecimalField(
        'Price', max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)]
        )

    def __str__(self):
        return self.name

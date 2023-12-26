from django.db import models
from django.core.validators import MinValueValidator


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.IntegerField(
        'Price', validators=[MinValueValidator(0)]
        )

    def __str__(self):
        return self.name

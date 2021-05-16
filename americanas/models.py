from django.db import models


class AmericanasProduct(models.Model):
    code = models.CharField(max_length=300)
    description = models.CharField(max_length=400)
    ean = models.IntegerField(default=None)


class ProductValues(models.Model):
    min_value = models.FloatField()
    product = models.ForeignKey(AmericanasProduct, on_delete=models.CASCADE)

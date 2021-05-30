from django.db import models


class Company(models.Model):
    description = models.CharField(max_length=300)


class Product(models.Model):
    code = models.CharField(max_length=300)
    description = models.CharField(max_length=400)
    ean = models.IntegerField(default=None)
    url = models.URLField(default="")
    image_url = models.URLField(default="")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default='')


class ProductMinValue(models.Model):
    min_value = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class WebSiteDivElement(models.Model):
    price_div = models.CharField(max_length=400)
    ame_div = models.CharField(max_length=400)
    description_div = models.CharField(max_length=400)




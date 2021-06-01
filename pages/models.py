import datetime
from django.db import models


class Company(models.Model):
    description = models.CharField(max_length=300, verbose_name="Descrição")
    date = models.DateTimeField(default=datetime.date.today)

    def __str__(self):
        return self.description


class Product(models.Model):
    code = models.CharField(max_length=300, verbose_name="Código")
    description = models.CharField(max_length=400, verbose_name="Descrição")
    ean = models.IntegerField(default=None)
    url = models.URLField(default="")
    image_url = models.URLField(default="", verbose_name="Url da imagem")
    date = models.DateTimeField(default=datetime.date.today)

    def __str__(self):
        return f'{self.code} - {self.description}'


class ProductMinValue(models.Model):
    min_value = models.FloatField(verbose_name="Valor Minimo")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Produto")
    company = models.ForeignKey(Company, on_delete=models.PROTECT, default='', verbose_name="Empresa")
    date = models.DateTimeField(default=datetime.date.today)

    def __str__(self):
        return f'{self.product.code} - {self.product.description} - {self.min_value}'


class WebSiteDivElement(models.Model):
    price_div = models.CharField(max_length=400, verbose_name="ID Preço")
    ame_div = models.CharField(max_length=400, verbose_name="ID Ame")
    description_div = models.CharField(max_length=400, verbose_name="ID Descrição")
    company = models.ForeignKey(Company, on_delete=models.PROTECT, default='', verbose_name="Empresa")

    def __str__(self):
        return f'{self.company.description} - {self.description_div}'

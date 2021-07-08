import datetime
from django.db import models


class Company(models.Model):
    description = models.CharField(max_length=300, verbose_name="Descrição")
    date = models.DateTimeField(default=datetime.date.today)
    web_site = models.CharField(max_length=300, default="")

    def __str__(self):
        return f"{self.description} - [{self.web_site}]"

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"


class Product(models.Model):
    code = models.CharField(max_length=300, verbose_name="Código")
    description = models.CharField(max_length=400, verbose_name="Descrição")
    # ean = models.IntegerField(default=None)
    url = models.URLField(default="")
    # image_url = models.URLField(default="", verbose_name="Url da imagem")
    date = models.DateTimeField(default=datetime.date.today)

    def __str__(self):
        return f'{self.code} - {self.description}'

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"


class ProductMinValue(models.Model):
    min_value = models.FloatField(verbose_name="Valor Minimo")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Produto")
    date = models.DateTimeField(default=datetime.date.today)

    def __str__(self):
        return f'{self.product.code} - {self.product.description} - {self.min_value}'

    class Meta:
        verbose_name = "Preço Minimo"
        verbose_name_plural = "Preços Minimos"


class WebSiteDivElement(models.Model):
    price_div = models.CharField(max_length=400, verbose_name="Class Preço")
    ame_div = models.CharField(max_length=400, verbose_name="Class Ame")
    description_div = models.CharField(max_length=400, verbose_name="Class Descrição")
    company = models.ForeignKey(Company, on_delete=models.PROTECT, default='', verbose_name="Empresa")

    def __str__(self):
        return f'{self.company.description} - {self.description_div}'

    class Meta:
        verbose_name = "Elemento Site"
        verbose_name_plural = "Elementos Site"


class ProductPriceHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    price = models.FloatField()
    date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f'{self.product.description} - {self.company.description}: {self.price}'

    class Meta:
        verbose_name = "Histórico de Preço"
        verbose_name_plural = "Históricos de Preços"

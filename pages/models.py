from django.db import models


class Company(models.Model):
    description = models.CharField(max_length=300)

    def __repr__(self):
        return self.description


class Product(models.Model):
    code = models.CharField(max_length=300, verbose_name="Código")
    description = models.CharField(max_length=400, verbose_name="Descrição")
    ean = models.IntegerField(default=None)
    url = models.URLField(default="")
    image_url = models.URLField(default="", verbose_name="Url da imagem")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default='', verbose_name="Empresa")


class ProductMinValue(models.Model):
    min_value = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class WebSiteDivElement(models.Model):
    price_div = models.CharField(max_length=400)
    ame_div = models.CharField(max_length=400)
    description_div = models.CharField(max_length=400)




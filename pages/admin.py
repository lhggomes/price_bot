from django.contrib import admin
from pages.models import *


@admin.register(Company)
class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ('description', 'web_site',)


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('description',)


@admin.register(WebSiteDivElement)
class WebSiteDivElementModelAdmin(admin.ModelAdmin):
    list_display = ('company', 'ame_div', 'description_div', 'price_div', )


@admin.register(ProductMinValue)
class ProductMinValueModelAdmin(admin.ModelAdmin):
    list_display = ('product', 'company', 'min_value',)


@admin.register(ProductPriceHistory)
class ProductPriceHistoryModelAdmin(admin.ModelAdmin):
    list_display = ('product', 'company', 'price')

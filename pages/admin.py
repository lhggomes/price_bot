from django.contrib import admin
from pages.models import *


# Register your models here.


@admin.register(Company)
class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ('description',)



from django.urls import path
from pages.views import *

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard-main'),
    path('dashboard/create-product', CreateProduct.as_view(), name='manage-product'),
]

from django.urls import path
from pages.views import *

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard-main'),
    path('dashboard/manage-product', ManageProduct.as_view(), name='manage-product'),
    path('dashboard/manage-company', ManageCompany.as_view(), name='manage-company'),
]

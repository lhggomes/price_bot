from django.urls import path
from pages.views import *

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard-main'),
    path('dashboard/manage-product', ManageProduct.as_view(), name='manage-product'),
    path('dashboard/manage-company', ManageCompany.as_view(), name='manage-company'),
    path('dashboard/manage-price', ManageMinPrice.as_view(), name='manage-min-price'),
    path('dashboard/manage-tech', ManageWebSiteDivs.as_view(), name='manage-tech'),



    path('dashboard/update-product/<int:pk>', UpdateProduct.as_view(), name='update-product'),
    path('dashboard/update-company/<int:pk>', UpdateCompany.as_view(), name='update-company'),
    path('dashboard/update-tech/<int:pk>', UpdateWebSiteDivs.as_view(), name='update-tech'),
]

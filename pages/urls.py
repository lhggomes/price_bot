from django.urls import path
from pages.views import *

urlpatterns = [
    # Create Views
    path('dashboard/', Dashboard.as_view(), name='dashboard-main'),
    path('dashboard/manage-product', ManageProduct.as_view(), name='manage-product'),
    path('dashboard/manage-company', ManageCompany.as_view(), name='manage-company'),
    path('dashboard/manage-price', ManageMinPrice.as_view(), name='manage-min-price'),
    path('dashboard/manage-tech', ManageWebSiteDivs.as_view(), name='manage-tech'),

    # Update Views
    path('dashboard/update/product/<int:pk>', UpdateProduct.as_view(), name='update-product'),
    path('dashboard/update/company/<int:pk>', UpdateCompany.as_view(), name='update-company'),
    path('dashboard/update/tech/<int:pk>', UpdateWebSiteDivs.as_view(), name='update-tech'),
    path('dashboard/update/price/<int:pk>', UpdateMinPrice.as_view(), name='update-price'),

    # Delete Views
    path('dashboard/delete/product/<int:pk>', DeleteProduct.as_view(), name='delete-product'),
    path('dashboard/delete/company/<int:pk>', DeleteCompany.as_view(), name='delete-company'),
    path('dashboard/delete/price/<int:pk>', DeleteMinPrice.as_view(), name='delete-price'),
    path('dashboard/delete/tech/<int:pk>', DeleteWebSiteDivs.as_view(), name='delete-tech'),

]

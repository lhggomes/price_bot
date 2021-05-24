from django.urls import path
from pages.views import Dashboard

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard-url'),
]

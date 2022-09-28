from django.urls import path

from core.erp.views import mi_primera_vista

urlpatterns = [
    path('uno/', mi_primera_vista),
]
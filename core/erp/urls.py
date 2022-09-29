from django.urls import path
from core.erp.views.categoria.views import lista_categoria

app_name = 'erp'

urlpatterns = [
    path('categoria/list/', lista_categoria, name='lista_categoria'),
]

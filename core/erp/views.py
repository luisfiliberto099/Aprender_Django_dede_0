from django.shortcuts import render

from core.erp.models import Categoria


def mi_primera_vista(request):
    date = {
        'name': 'Luis',
        'Categoria': Categoria.objects.all()
    }
    return render(request, 'home.html', date)
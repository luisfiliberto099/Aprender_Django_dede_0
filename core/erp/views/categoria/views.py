from django.shortcuts import render


def lista_categoria(request):
    data = {

    }
    return render(request, 'categoria/list.html', data)
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Receita


def index(request):
    receitas = Receita.objects.all()

    # receitas = {
    #     1:'Lasanha',
    #     2:'Sopa',
    #     3:'Sorvete ',
    #     4:'Bolo'
    # }
    dados = {
        'receitas': receitas
    }
    return render(request, 'index.html', dados)


def receita(request, receita_id):
    r = get_object_or_404(Receita, pk=receita_id)
    receita_a_exibir = {
        'receita': r
    }
    return render(request, 'receita.html', receita_a_exibir)

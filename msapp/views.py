from django.shortcuts import render


def index(request):

    produtos = {
        1:'Arroz',
        2:'Feijão',
        3:'Creme de leite',
    }
    dados = {
        'nome_dos_alimentos': produtos
    }
    return render(request,'index.html', dados)


def produtos(request):
    return render(request, 'produtos.html')


def sobre(request):
    return render(request, 'sobre.html')

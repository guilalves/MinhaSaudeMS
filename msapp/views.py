from django.shortcuts import render


def index(request):
    return render(request,'index.html')


def produtos(request):
    return render(request, 'produtos.html')


def sobre(request):
    return render(request, 'sobre.html')

from django.shortcuts import render
   

# Create your views here.

def index(request):

    receitas = {
        1: 'Lasanha',
        2: 'Sopa de Legumes',
        3: 'Sorvete de Morango',
        4: 'Sufle de Batata'
    }
    dados = {
        'nome_das_receitas' : receitas
    }
    return render(request,'index.html', dados)

def receita(request):
    return render(request,'receita.html')   



from django.forms import PasswordInput
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if not nome.strip():
            print('Invalid name')
            return redirect('cadastro')

        if not email.strip():
            print('Email inválido')
            return redirect('cadastro')

        if password != password2:
            print('senhas não são iguais')
            return redirect('cadastro')

        if User.objects.filter(email = email).exists():
            print('Usuario já cadastrado')
            return redirect('cadastro')

        user = User.objects.create_user(username = nome,
                                        email = email,
                                        password = password)
        user.save()

        print('Usuario cadastrado com sucesso')


        print(nome, email, password, password2)
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == '' or senha == '':
            print('Dados inválidos!')
            return redirect('login')
        print(email, senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat = True).get()
            user = auth.authenticate(request, username = nome, password = senha)
            if user is not None:
                auth.login(request, user)
                print('login realizado com sucesso')
                return redirect('dashboard')
    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/dashboard.html')
    else:
        return redirect('index')
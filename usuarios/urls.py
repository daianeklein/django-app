from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name = 'login'),
    path('dashboard', views.dashboard, name ='dashboard'),
    path('logout', views.logout, name='logout'),
    path('cria_receita', views.cria_receita, name='cria_receita')

]
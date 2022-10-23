
#from escola.views import ListaALunosMatriculados
from escola.views import ListaALunosMatriculados

from escola.models import Matricula
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from escola.views import AlunosViewSet, CursosViewSet, MatriculaViewSet, ListaMetriculasAlunos
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename= 'Alunos')
router.register('cursos', CursosViewSet, basename= 'Cursos')
router.register('matriculas', CursosViewSet, basename= 'Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/', ListaMetriculasAlunos.as_view()),
    path('curso/<int:pk>/matriculas/', ListaALunosMatriculados.as_view())
]

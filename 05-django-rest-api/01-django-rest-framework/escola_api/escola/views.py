from rest_framework import viewsets
from escola.models import Aluno, Curso
from .serializer import AlunoSerializer, CursoSerializer

# from django.http import JsonResponse

# def alunos(request):
#     if request.method == 'GET':
#         aluno = {'id': 1,
#             'nome' : 'Daiane'}
#         return JsonResponse(aluno)

class AlunosViewSet(viewsets.ModelViewSet):
    '''Exibe todos os alunos e alunas'''
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    '''Exibe todos os cursos'''
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


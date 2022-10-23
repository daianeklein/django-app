from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from .serializer import AlunoSerializer, CursoSerializer, ListaMatriculasAlunoSerializer, MatriculaSerializer, ListaAlunosMatriculadosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

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
    authentication_classes =  [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CursosViewSet(viewsets.ModelViewSet):
    '''Exibe todos os cursos'''
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    '''Lista todas as matrículas'''
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMetriculasAlunos(generics.ListAPIView):
    '''Lista as matrículas de um aluno ou aluna'''
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id = self.kwargs['pk'])
        return queryset

    serializer_class = ListaMatriculasAlunoSerializer


class ListaALunosMatriculados(generics.ListAPIView):
    '''Lista alunos e alunas matriculados em um curso'''
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk'])

        return queryset

    serializer_class = ListaAlunosMatriculadosSerializer


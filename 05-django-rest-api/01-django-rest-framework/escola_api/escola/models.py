from email.policy import default
from pyexpat import model
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length = 100)
    rg = models.CharField(max_length = 9)
    cpf = models.CharField(max_length = 11)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

class Curso(models.Model):
    NIVEL = (
        ('B', 'Basico'),
        ('I', 'Intermediario'),
        ('A', 'Avancado')
)

    codigo_curso = models.CharField(max_length = 10)
    descricao = models.CharField(max_length = 100)
    nivel = models.CharField(max_length = 1, choices = NIVEL, blank = False, null = False, default = 'B')

    def __str__(self):
        return self.descricao
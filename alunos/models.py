from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    matricula = models.CharField(max_length=20  , unique=True)

    def __str__(self):
        return f"{self.nome} ({self.matricula})"

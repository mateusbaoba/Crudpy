from django.shortcuts import render

from alunos.models import Aluno
from disciplinas.models import Disciplina

from django.db.models import Count

disciplinas = Disciplina.objects.annotate(
    total_matriculas=Count("alunos")).order_by("nome")

# Create your views here.
def home(request):
    return render(
        request,
        "dashboard/home.html",
        {
            "total_alunos": Aluno.objects.count(),
            "total_disciplinas": Disciplina.objects.count(),
            "matriculas_por_disciplina": [
                {"nome": disciplina.nome, "total": disciplina.total_matriculas}
                for disciplina in disciplinas
            ],
        },
    )
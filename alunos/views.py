from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .forms import AlunoForm
from .models import Aluno
# Create your views here.

@login_required
def lista(request):
    alunos = Aluno.objects.all().order_by("nome")
    return render(request, "alunos/aluno_list.html", {"alunos": alunos})

@login_required
def criar(request):
    form = AlunoForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("alunos:lista")

    return render(request, "alunos/aluno_form.html", {"form": form})

@login_required
def editar(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    form = AlunoForm(request.POST or None, instance=aluno)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("alunos:lista")

    return render(request, "alunos/aluno_form.html", {"form": form})

@login_required
def excluir(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)

    if request.method == "POST":
        aluno.delete()
        return redirect("alunos:lista")

    return render(request, "alunos/aluno_confirm_delete.html", {"aluno": aluno})

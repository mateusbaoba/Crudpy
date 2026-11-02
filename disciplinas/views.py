from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .forms import DisciplinaForm, MatriculaForm
from .models import Disciplina

# Create your views here.

def lista(request):
    disciplinas = Disciplina.objects.all()
    return render(request, 
                  "disciplinas/disciplina_list.html", 
                  {"disciplinas": disciplinas})

def criar(request):
    form = DisciplinaForm(request.POST or None)
    if form == "POST":        
        if form.is_valid():
            form.save()
            return redirect("disciplinas:lista")
   
    return render(request, 
                  "disciplinas/disciplina_form.html", 
                  {"form": form})

def detalhe(request, pk):
    disciplina = get_object_or_404(Disciplina, pk=pk)
    alunos = disciplina.alunos.order_by("nome")

    return render(request,
                    "disciplinas/disciplina_detalhe.html", 
                    {"disciplina": disciplina, "alunos": alunos})

def matricular(request, pk):
    disciplina = get_object_or_404(Disciplina, pk=pk)
    form = MatriculaForm(request.POST or None, disciplina=disciplina)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("disciplinas:detalhe", pk=disciplina.pk)

    return render(request,
                  "disciplinas/matricular.html",
                  {"form": form, 
                   "disciplina": disciplina,
                   "alunos": disciplina.alunos.order_by("nome")
                   })
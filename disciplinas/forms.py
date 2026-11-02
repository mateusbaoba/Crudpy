from django import forms

from alunos.models import Aluno
from .models import Disciplina

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['id', 'nome', 'descricao', 'carga_horaria']


class MatriculaForm(forms.Form):
    alunos = forms.ModelMultipleChoiceField(
        queryset=Aluno.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Alunos sem disciplina",
    )

    def __init__(self, *args, disciplina, **kwargs):
        super().__init__(*args, **kwargs)
        self.disiplina = disciplina
        self.fields['alunos'].queryset = (
            Aluno.objects.filter(disciplina__isnull=True)
        )

    def save(self):
        return Aluno.objects.filter(
            pk__in=self.cleaned_data['alunos'],
            disciplina__isnull=True,
        ).update(disciplina=self.disiplina)
# Crudpy

Aplicacao CRUD de alunos desenvolvida com Django. Permite cadastrar, listar,
editar e excluir alunos. As telas de alunos exigem autenticacao.

## Requisitos

- Python 3.12 ou superior
- pip

## Como executar

No Windows, abra o terminal na pasta do projeto e execute:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Abra http://127.0.0.1:8000/contas/login/ e entre com o superusuario criado.

## Configuracao

`DJANGO_SECRET_KEY` pode ser definida como variavel de ambiente. Para uso local,
o projeto possui uma chave de desenvolvimento padrao; defina uma chave propria
em ambientes compartilhados ou de producao.

O banco SQLite local (`db.sqlite3`) e arquivos de ambiente nao sao versionados.

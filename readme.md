# Controle de gastos

## Rodando localmente

Primeiro clone o repositorio

```bash
    git clone https://github.com/ViniciusCosta126/gastos-django
```

Depois de clonado entre na pasta

```bash
    cd gastos-django
```

Crie a virtualenv para instalar as libs

```bash
    python3 -m venv env
```

Instale as libs
```bash
    pip install -r requirements.txt
``` 

Para iniciar o servidor rode:
```bash
    python3 manage.py runserver
```
Faça as migrations para o banco de dados
```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
```

Rode o comando para pegar todos os arquivos estaticos
```bash
    python3 manage.py collectstatic
```
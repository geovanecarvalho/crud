# Teste Geobit - Crud

Sistema em django para implementação de crud.

## Requirementos

* [Django](https://www.djangoproject.com/)
* [Git](http://git-scm.com/)
* [Python](https://www.python.org/)
* [Pip](http://www.pip-installer.org/en/latest/)
* [Virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)

## Configuração de Ambiente

### **Instalando todas as dependências**

```
$ mkvirtualenv crud-geobit -p python3
$ pip install -r requirements.txt
```

### Carregado os dados
```
$ python manage.py migrate
```
### Teste
```
python manage.py test
```
### Criar usuário para login no sistema
```
$ python manage.py createsuperuser
```

## Executando o Projeto
```
$ python manage.py runserver
```
Após subir o Django, verifique na porta 8000:
*http://localhost:8000/admin*

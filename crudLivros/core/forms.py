from django import forms
from .models import Autor, Livro

#formulário para cadastro de autor
class AutorForm(forms.ModelForm):
	class Meta:

		model = Autor
		fields = ['nome']

		widgets = {
			'nome': forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Digite o nome do autor do livro'},)
		}

#formulário para cadastro de Livro
class LivroForm(forms.ModelForm):
	class Meta:

		model = Livro
		fields = ['nome', 'quantidade_pagina', 'preco', 'data_inclusao', 'autor']

		widgets = {
			'nome': forms.TextInput(attrs={'class':'form-control' ,'placeholder':'Digite o nome do livro'},),
			'quantidade_pagina': forms.NumberInput(attrs={'class':'form-control' ,'placeholder':'Quantidade de Página'},),
			'preco': forms.NumberInput(attrs={'class':'form-control' ,'placeholder':'R$ 0,00', 'type':'number'},),
			'data_inclusao': forms.DateInput(attrs={'class':'form-control' ,'placeholder':'Data Ex: 02/06/2000', 'type':'date'},),
			'autor': forms.Select(attrs={'class':'form-control' },),						
		}
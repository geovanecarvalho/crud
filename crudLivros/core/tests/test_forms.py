from django.test import TestCase
from ..forms import AutorForm

#Teste Formulario Autor
class AutorFormTest(TestCase):
	def teste_cadastro_autor(self):
		form = AutorForm(data={
			'nome': 'William'
			})
		self.assertTrue(form.is_valid())

#Teste Formulario livro
class LivroFormTest(TestCase):
	def teste_cadastro_autor(self):
		form = AutorForm(data={
			'nome': 'A cabana',
			'quantidade_pagina':'50',
			'preco':'10.50',
			'data_inclusao':'02/06/2020',
			'autor':"William"

			})
		self.assertTrue(form.is_valid())


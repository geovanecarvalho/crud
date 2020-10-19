from django.test import TestCase
from ..models import Autor, Livro

#teste tabela autor
class AutorModelTest(TestCase):
	def setUp(self):
		self.autor = Autor(nome='William')
	def test_str_autor(self):
		self.assertEqual(str(self.autor), 'William')


#teste tabela livro
class LivroModelTest(TestCase):
	def setUp(self):
		self.autor = Autor.objects.create(nome="William")
		self.livro = Livro.objects.create(
			nome = 'A Cabana',
			quantidade_pagina=50,
			preco=1,
			data_inclusao='2020-10-18',
			autor=self.autor
			)
	
	def test_str_livro(self):
		self.assertEqual(str(self.livro), 'A Cabana')

	
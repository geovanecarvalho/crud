from django.test import TestCase
from django.urls import reverse
from ..models import Autor, Livro

#teste template index
class HomeViewTest(TestCase):
	def test_status_code_200(self):
		response = self.client.get(reverse('home'))
		self.assertEquals(response.status_code, 200)

	def test_template(self):
		response = self.client.get(reverse('home'))
		self.assertTemplateUsed(response, 'index.html')

#teste template cadastro autor
class AutorViewTest(TestCase):
	def test_status_code_200(self):
		response = self.client.get(reverse('autor'))
		self.assertEquals(response.status_code, 200)

	def test_template(self):
		response = self.client.get(reverse('autor'))
		self.assertTemplateUsed(response, 'autor.html')

#teste template cadastro livro
class LivroViewTest(TestCase):
	def test_status_code_200(self):
		response = self.client.get(reverse('livro'))
		self.assertEquals(response.status_code, 200)

	def test_template(self):
		response = self.client.get(reverse('livro'))
		self.assertTemplateUsed(response, 'livro.html')

#teste template update 
class UpdateViewTest(TestCase):
	def test_status_code_200(self):
		response = self.client.get(reverse('update'))
		self.assertEquals(response.status_code, 200)

	def test_template(self):
		response = self.client.get(reverse('update'))
		self.assertTemplateUsed(response, 'update.html')

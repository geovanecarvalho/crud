from django.db import models
from django.core.validators import  MinValueValidator


class Autor(models.Model):
	nome = models.CharField(max_length=50, unique=True)

	class Meta:
		verbose_name = "Autor"
		verbose_name_plural = "Autores"

	def __str__(self):
		return self.nome


class Livro(models.Model):
	nome = models.CharField(max_length=50, unique=True)
	quantidade_pagina = models.PositiveIntegerField("Quantidade de Página")
	preco = models.DecimalField("preço", max_digits=10, decimal_places=2, validators = [MinValueValidator(1)] )
	data_inclusao = models.DateField("Data de Inclusão")
	autor = models.ForeignKey("Autor", on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Livro"
		verbose_name_plural = "Livros"

	def __str__(self):
		return self.nome

	

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AutorForm, LivroForm
from .models import Livro, Autor
# Create your views here.

def home(request):
	obj = Livro.objects.all()
	autor = Autor.objects.all()

	return render(request, 'index.html', {'obj': obj, 'autor': autor})


def autor(request):
	form = AutorForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('livro.html')
	
	
	return render(request, 'autor.html', {'form': form})

def livro(request):
	form = LivroForm
	return render(request, 'livro.html', {'form': form})
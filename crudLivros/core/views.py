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
		return redirect('/autor/')
	
	return render(request, 'autor.html', {'form': form})

def update_autor(request, id):
	obj = Autor.objects.get(id=id)
	form = AutorForm(request.POST or None, instance=obj)
	
	if form.is_valid():
		form.save()
		return redirect('/')

	return render(request, 'autor.html', {'form': form, 'obj': obj})

def delete_autor(request, id):
	obj = Autor.objects.get(id=id)

	if request.method == 'POST':
		obj.delete()
		return redirect('/')
	return render(request, 'auto-delete-confirma.html', {'obj': obj})


def livro(request):
	form = LivroForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/livro/')	
	return render(request, 'livro.html', {'form': form})

def update_livro(request, id):
	obj = Livro.objects.get(id=id)
	form = LivroForm(request.POST or None, instance=obj)
	
	if form.is_valid():
		form.save()
		return redirect('/')

	return render(request, 'livro.html', {'form': form, 'obj': obj})

def delete_livro(request, id):
	obj = Livro.objects.get(id=id)

	if request.method == 'POST':
		obj.delete()
		return redirect('/')
	return render(request, 'auto-delete-confirma.html', {'obj': obj})


def update(request):
	obj = Autor.objects.all()
	return render(request, 'update.html', {'obj': obj})
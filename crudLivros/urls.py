"""crudLivros URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crudLivros.core.views import home, autor, livro, update_autor, delete_autor, update_livro, delete_livro, update

urlpatterns = [
	path('', home),
	path('autor/', autor),
    path('update/autor/<int:id>/', update_autor),
    path('delete/autor/<int:id>/', delete_autor),
    path('update', update),
	
    path('livro/', livro),
    path('update/livro/<int:id>/', update_livro),
    path('delete/livro/<int:id>/', delete_livro),
    path('admin/', admin.site.urls),
]

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
from crudLivros.core import views
urlpatterns = [
	path('', views.home),
	path('autor/', views.autor),
    path('update/autor/<int:id>/', views.update_autor),
    path('delete/autor/<int:id>/', views.delete_autor),
    path('update', views.update),
	
    path('livro/', views.livro),
    path('update/livro/<int:id>/', views.update_livro),
    path('delete/livro/<int:id>/', views.delete_livro),
    path('admin/', admin.site.urls),
]

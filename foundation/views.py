from django.shortcuts import render

from .models import *

menu = ['Главная', 'Книги', 'Обновления', 'Популярное', 'Завершенные романы', 'Коталог жанров', 'Поиск по тегам', 'Форум', 'Новости сайта', 'Контакты', 'Правила']

def home(request):
    posts = Case.objects.all()
    return render(request, 'foundation/home.html', {'posts': posts, 'menu': menu, "title": 'Главная страница'})

def categories(request):
    return render(request, 'foundation/home')



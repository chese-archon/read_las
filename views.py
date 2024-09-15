from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Обработка https запросов и функции представления для страниц Главная & other

#def home(request):
#    return HttpResponse('<h1>Главная</h1>')

def audio(request):
    return HttpResponse('<h1>Аудио</h1>')

def video(request):
    return HttpResponse('<h1>Видео</h1>')

def afisha(request):
    return HttpResponse('<h1>Афиша</h1>')

def news(request):
    return HttpResponse('<h1>Новости</h1>')

#def bio(request):
#    return HttpResponse('<h1>Биография</h1>')

def contacts(request):
    return HttpResponse('<h1>Контакты</h1>')


posts = [
    {
        'author': 'Администратор',
        'title': 'Это первый пост',
        'content': 'Содержание первого поста.',
        'date_posted': '12 мая, 2022'
    },
    {
        'author': 'Пользователь',
        'title': 'Это второй пост',
        'content': 'Подробное содержание второго поста.',
        'date_posted': '13 мая, 2022'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context)


def bio(request):
    return render(request, 'about.html', {'title': 'О клубе Python Bytes'})

import json
import laspy
def las_old(request):
    path = "C:/Users/irin3/PycharmProjects/pythonProject6/pythonProject3/pashtech/pashtech_site/pashtech_app/templates/serpent-small.las"

    # Чтение файла .las
    las = laspy.read(path)
    points = []

    # Извлечение координат точек (X, Y, Z)
    for x, y, z in zip(las.x, las.y, las.z):
        points.append({'x': x, 'y': y, 'z': z})

    # Конвертируем в JSON и передаем в шаблон
    return render(request, 'tpy.html', {'points': json.dumps(points)})
    #return render(request, 'las_show.html')

def las2(request):
    path = "C:/Users/irin3/PycharmProjects/pythonProject6/pythonProject3/pashtech/pashtech_site/pashtech_app/templates/serpent-small.las"

    # Чтение файла .las
    las = laspy.read(path)
    points = []

    for x, y, z, r, g, b in zip(las.x, las.y, las.z, las.red, las.green, las.blue):
        points.append({
            'x': x,
            'y': y,
            'z': z,
            'r': r / 65535,  # Нормализуем цветовые значения в диапазон от 0 до 1
            'g': g / 65535,
            'b': b / 65535
        })# just black canvas

    # Конвертируем в JSON и передаем в шаблон
    return render(request, 'tpy2.html', {'points': json.dumps(points)})

def las3(request):
    path = "C:/Users/irin3/PycharmProjects/pythonProject6/pythonProject3/pashtech/pashtech_site/pashtech_app/templates/serpent-small.las"

    # Чтение файла .las
    las = laspy.read(path)
    points = []

    for x, y, z, r, g, b in zip(las.x, las.y, las.z, las.red, las.green, las.blue):
        points.append({
            'x': x,
            'y': y,
            'z': z,
            'r': r / 65535,  # Нормализуем цветовые значения в диапазон от 0 до 1
            'g': g / 65535,
            'b': b / 65535
        })# just black canvas

    # Конвертируем в JSON и передаем в шаблон
    return render(request, 'tpy3.html', {'points': json.dumps(points)})

def las4(request):
    path = "C:/Users/irin3/PycharmProjects/pythonProject6/pythonProject3/pashtech/pashtech_site/pashtech_app/templates/serpent-small.las"

    # Чтение файла .las
    las = laspy.read(path)
    points = []

    for x, y, z, r, g, b in zip(las.x, las.y, las.z, las.red, las.green, las.blue):
        points.append({
            'x': x,
            'y': y,
            'z': z,
            'r': r / 65535,  # Нормализуем цветовые значения в диапазон от 0 до 1
            'g': g / 65535,
            'b': b / 65535
        })# just black canvas

    # Конвертируем в JSON и передаем в шаблон
    return render(request, 'tpy4.html', {'points': json.dumps(points)})

def las(request):
    path = "C:/Users/irin3/PycharmProjects/pythonProject6/pythonProject3/pashtech/pashtech_site/pashtech_app/templates/serpent-small.las"

    # Чтение файла .las
    las = laspy.read(path)
    points = []

    for x, y, z, r, g, b in zip(las.x, las.y, las.z, las.red, las.green, las.blue):
        points.append({
            'x': x,
            'y': y,
            'z': z,
            'r': r / 65535,  # Нормализуем цветовые значения в диапазон от 0 до 1
            'g': g / 65535,
            'b': b / 65535
        })# just black canvas

    # Конвертируем в JSON и передаем в шаблон
    return render(request, 'tpy5.html', {'points': json.dumps(points)})
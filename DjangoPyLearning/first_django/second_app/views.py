from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
import datetime


def dictsort(request):
    context = {"questions": [{'priority': 100, 'task': 'Составить список дел'},
                             {'priority': 150, 'task': 'Изучать Django'},
                             {'priority': 1, 'task': 'Подумать о смысле жизни'}]}
    return render(template_name='second_app/bootstrap.html', request=request, context=context)


def main_page(request):
    return render(request, 'second_app/main.html')


def about(request):
    return render(request, 'second_app/about.html')


def contacts(request):
    return render(request, 'second_app/contacts.html')


def news(request):
    return render(request, 'second_app/news.html')


def rulers(request):
    return render(request, 'second_app/rulers.html')

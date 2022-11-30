from django.shortcuts import render


def main_page(request):
    return render(request, 'main.html')


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contacts.html')


def news(request):
    return render(request, 'news.html')


def rulers(request):
    return render(request, 'rulers.html')
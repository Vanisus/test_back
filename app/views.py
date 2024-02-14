from django.shortcuts import render


def home(request):
    return render(request, 'app/home.html')


def first(request):
    return render(request, 'app/first.html')


def second(request):
    return render(request, 'app/second.html')

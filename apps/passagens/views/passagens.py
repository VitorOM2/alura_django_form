from django.shortcuts import render


def index(request):
    """ Configura a view index """
    return render(request, 'index.html')

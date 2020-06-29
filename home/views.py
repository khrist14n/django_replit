from django.http import HttpResponse


def index(request):
    message = '<h1>App de Django</h1>'
    return HttpResponse(message)


def home(request):
    message = '<h1>Home de Django</h1>'
    message = message + "<p>Informacion de Django</p>"
    return HttpResponse(message)

def link(request):
    message = '<h1>Enlace de Django</h1>'
    message = message + "<p>Enlace de Django</p>"
    return HttpResponse(message)    
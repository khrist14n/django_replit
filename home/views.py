from django.http import HttpResponse


def index(request):
    message = 'App de Django'
    return HttpResponse(message)
    
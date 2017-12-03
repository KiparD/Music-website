from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>This is a Music app homepage</h1>")

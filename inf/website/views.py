from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You are on INF (future) website.")

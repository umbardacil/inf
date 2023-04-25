from django.shortcuts import HttpResponse
from django.utils.translation import gettext as _


def index(request):
    return HttpResponse(_("Hello, world. You are on INF (future) website."))

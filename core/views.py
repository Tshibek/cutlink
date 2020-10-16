from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import UrlShortcut
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'core/home.html'




def shortcutCreate(request):
    pass


def shortcutShow(request, slug):
    url = get_object_or_404(UrlShortcut, short=slug)
    url.clicked()
    return redirect(url.link)


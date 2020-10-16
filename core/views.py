from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import UrlShortcut
from django.views.generic.base import TemplateView
from .forms import ShortCutForm

class HomePageView(TemplateView):
    template_name = 'core/home.html'




def shortcutCreate(request):
    template = 'core/CreateShortCut.html'
    if request.method == 'POST':
        form = ShortCutForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            short = form.save(commit=False)
            short.save()

    else:
        form = ShortCutForm()

    context = locals()
    return render(request, template, context=context )



def shortcutShow(request, slug):
    url = get_object_or_404(UrlShortcut, short=slug)
    url.clicked()
    return redirect(url.link)


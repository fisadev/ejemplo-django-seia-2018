from django.shortcuts import render
from sitio.models import Noticia
from sitio.forms import FormNoticia, FormNoticiaMagico
from datetime import datetime


def inicio(request):
    nueva = Noticia()
    nueva.titulo = 'entro alguien!'
    nueva.texto = 'acaba de entrar alguien al sitio'
    nueva.fecha = datetime.now()
    nueva.save()

    noticias = Noticia.objects.all()
    return render(request, 'inicio.html',
                  {'lista_noticias': noticias})

def form_a_la_antigua(request):
    print("vino esto en el post:", request.POST)
    print("vino esto en el get:", request.GET)
    return render(request, 'form_a_la_antigua.html', {})


def form_un_poco_mejor(request):
    print("vino esto en el post:", request.POST)
    print("vino esto en el get:", request.GET)

    form = FormNoticia()
    if request.method == "POST":
        form = FormNoticia(request.POST)
        if form.is_valid():
            print('Form data:', form.cleaned_data)

    return render(request, 'form_un_poco_mejor.html', {'form': form})

def form_posta(request):
    print("vino esto en el post:", request.POST)
    print("vino esto en el get:", request.GET)

    form = FormNoticiaMagico()
    if request.method == "POST":
        form = FormNoticiaMagico(request.POST)
        if form.is_valid():
            print('Form data:', form.cleaned_data)
            form.save()

    return render(request, 'form_posta.html', {'form': form})

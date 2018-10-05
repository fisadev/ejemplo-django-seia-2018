from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import viewsets

from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from sitio.models import Noticia, Categoria
from sitio.forms import FormNoticia, FormNoticiaMagico
from sitio.serializers import NoticiaSerializer, CategoriaSerializer
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


def ejemplo_apis(request):
    return render(request, 'ejemplo_apis.html', {})


def api_cantidad_noticias(request):
    data = {
        'cantidad_noticias': Noticia.objects.count()
    }
    return JsonResponse(data)


def ajax_noticias_recientes(request):
    datos = {
        'lista_noticias': Noticia.objects.order_by('-fecha')[:3]
    }
    return render(request, 'noticias_recientes.html', datos)



class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by('nombre')
    serializer_class = CategoriaSerializer


class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.all().order_by('-fecha')
    serializer_class = NoticiaSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    filter_fields = ('archivada', 'categoria')

"""noticias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from sitio import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('categorias', views.CategoriaViewSet)
router.register('noticias', views.NoticiaViewSet)


urlpatterns = [
    path('inicio/', views.inicio),
    path('form_a_la_antigua/', views.form_a_la_antigua),
    path('form_un_poco_mejor/', views.form_un_poco_mejor),
    path('form_posta/', views.form_posta),
    path('ejemplo_apis/', views.ejemplo_apis),
    path('api/cantidad_noticias/', views.api_cantidad_noticias),
    path('ajax/noticias_recientes/', views.ajax_noticias_recientes),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('search/', include('haystack.urls')),
]

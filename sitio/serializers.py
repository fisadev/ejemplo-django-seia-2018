from rest_framework import serializers

from sitio.models import Noticia, Categoria


class NoticiaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Noticia
        fields = ('url', 'titulo', 'texto', 'fecha', 'archivada', 'categoria')


class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ('url', 'nombre', )

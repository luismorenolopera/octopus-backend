from rest_framework_mongoengine.viewsets import ModelViewSet
from recetas.models import Autor, Receta
from recetas.serializers import AutorSerializer, RecetaSerializer


class AutorViewSet(ModelViewSet):
    lookup_field = 'id'
    serializer_class = AutorSerializer
    queryset = Autor.objects()


class RecetaViewSet(ModelViewSet):
    lookup_field = 'id'
    serializer_class = RecetaSerializer
    queryset = Receta.objects()

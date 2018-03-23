from rest_framework_mongoengine import serializers
from recetas.models import Autor, Receta


class AutorSerializer(serializers.DynamicDocumentSerializer):
    class Meta:
        model = Autor
        fields = '__all__'


class RecetaSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Receta
        fields = '__all__'

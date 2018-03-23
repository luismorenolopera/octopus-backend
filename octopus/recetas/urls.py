from django.urls import path, include
from rest_framework_mongoengine.routers import DefaultRouter
from recetas.views import RecetaViewSet, AutorViewSet


router = DefaultRouter()
router.register(r'recetas', RecetaViewSet)
router.register(r'autores', AutorViewSet)

urlpatterns = [
    path('', include(router.urls))
]

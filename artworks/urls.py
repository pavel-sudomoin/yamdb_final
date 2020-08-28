from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, GenreViewSet
from .views import TitleViewSet


v1_router = DefaultRouter()
v1_router.register(
    'categories',
    CategoryViewSet,
    basename='Category'
)
v1_router.register(
    'genres',
    GenreViewSet,
    basename='Genre'
)
v1_router.register(
    'titles',
    TitleViewSet,
    basename='Title'
)

urlpatterns = [
    path('', include(v1_router.urls))
]

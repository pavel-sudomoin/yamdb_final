from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets, filters, mixins

from .models import Category, Genre, Title
from .serializers import CategorySerializer, GenreSerializer
from .serializers import TitleSerializer
from users.rbac import AnyoneCanSeeListAdminCanEdit
from .filters import TitleFilter


class BaseCreateDeleteListViewSet(
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    pass


class CategoryViewSet(BaseCreateDeleteListViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=name',)
    permission_classes = (AnyoneCanSeeListAdminCanEdit,)


class GenreViewSet(BaseCreateDeleteListViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'slug'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=name',)
    permission_classes = (AnyoneCanSeeListAdminCanEdit,)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter
    permission_classes = (AnyoneCanSeeListAdminCanEdit,)

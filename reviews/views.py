from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext_lazy as _
from rest_framework import viewsets, serializers
from rest_framework.pagination import PageNumberPagination
from .models import Review, Comment, Title
from .serializers import ReviewSerializer, CommentSerializer
from users.rbac import (
    AnyoneCanSeeAdminModerAuthorCanEdit,
    AnyoneCanSeeListAdminCanEdit,
)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination
    permission_classes = (AnyoneCanSeeAdminModerAuthorCanEdit,)

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination
    permission_classes = (AnyoneCanSeeAdminModerAuthorCanEdit,)

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(
            Review,
            pk=self.kwargs.get('review_id'),
            title__id=self.kwargs.get('title_id'),
        )
        serializer.save(author=self.request.user, review=review)

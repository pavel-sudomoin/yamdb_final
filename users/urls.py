from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

from .views import (
    CreateUserView,
    GenerateTokenByConfCodeAndEmail,
    UsersView,
    CabinetView,
)


router = DefaultRouter()
router.register('users', UsersView, basename='users')

urlpatterns = [
    path('users/me/', CabinetView.as_view(), name='cabinet_view'),
    path('', include(router.urls)),
    path('auth/email/', CreateUserView.as_view(), name='create_user'),
    path(
        'auth/token/',
        GenerateTokenByConfCodeAndEmail.as_view(),
        name='create_token',
    ),
]

urlpatterns += [
    path(
        'auth/token/obtain/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair',
    ),
    path(
        'auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'
    ),
]

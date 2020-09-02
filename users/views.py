from rest_framework.views import APIView
from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework import permissions, status, generics
from rest_framework.exceptions import ValidationError, ParseError
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
import uuid
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken

from .rbac import AdminUserCanDoAnything
from .serializers import UserSerializerForAdmin, UserSerializerForUsers

User = get_user_model()


class CabinetView(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return UserSerializerForAdmin
        return UserSerializerForUsers


class UsersView(viewsets.ModelViewSet):
    serializer_class = UserSerializerForAdmin
    permission_classes = (AdminUserCanDoAnything,)
    queryset = User.objects.all()
    lookup_field = 'username'


class CreateUserView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        email = request.data.get('email')
        if email is None:
            raise ValidationError(_('Email is empty'))
        email = email.strip()
        confirmation_code = str(uuid.uuid4())
        user, is_created = User.objects.get_or_create(
            email=email, defaults={'confirmation_code': confirmation_code}
        )

        send_mail(
            _('Account created/updated'),
            _('Now you can login with confirmation_code:') + confirmation_code,
            user.email,
            ['email'],
            fail_silently=True,
        )
        return Response(status=status.HTTP_202_ACCEPTED)


class GenerateTokenByConfCodeAndEmail(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        email = request.data.get('email')
        confirmation_code = request.data.get('confirmation_code')
        if email is None or confirmation_code is None:
            raise ParseError(_('Not all fields are set'))
        user = get_object_or_404(
            User, email=email, confirmation_code=confirmation_code
        )
        refresh = RefreshToken.for_user(user)
        return Response(
            {'token': str(refresh.access_token)}, status=status.HTTP_200_OK
        )

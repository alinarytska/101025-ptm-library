from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from library.models import User
from library.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'], url_path='get-me')
    def get_me(self, request: Request, *args, **kwargs) -> Response:
        obj = get_object_or_404(User, pk=request.user.pk)
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

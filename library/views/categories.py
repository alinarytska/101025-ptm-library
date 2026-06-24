from rest_framework.viewsets import ModelViewSet

from library.models import Category
from library.serializers.category import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

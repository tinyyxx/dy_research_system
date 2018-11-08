from .models import CategoryModel
from rest_framework import mixins, viewsets
from .serializers import CategorySerializer
# Create your views here.


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    api接口获取所有的左侧目录及子目录的view
    """
    queryset = CategoryModel.objects.filter(category_type=1)
    serializer_class = CategorySerializer

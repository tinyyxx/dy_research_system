from .models import CategoryModel
from rest_framework import mixins, viewsets
from rest_framework.views import APIView
from .serializers import CategorySerializer, GetIndexSerializer
from rest_framework.response import Response
# Create your views here.


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    api接口获取所有的左侧目录及子目录的view
    """
    queryset = CategoryModel.objects.filter(parent_category=None)               # filter(category_type=1)
    serializer_class = CategorySerializer


class GetIndexView(APIView):
    """
    xadmin后台管理系统获取目录管理中定义好的指标
    """
    queryset = CategoryModel.objects.all()

    def get(self, request):
        index_list = GetIndexSerializer(self.queryset, many=True)
        return Response(index_list.data)


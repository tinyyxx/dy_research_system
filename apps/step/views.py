from django.shortcuts import render
from .models import StepModel
from rest_framework import mixins, viewsets, status
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly
from .serializers import StepSerializer
from .serializers import StepDataSerializer
from . import StepData
from rest_framework.response import Response
from utils.getdata import search
from datetime import datetime
# Create your views here.


class StepViewSet(viewsets.ModelViewSet): # mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin,viewsets.GenericViewSet):
    """
    list、retrieve、destroy 相应step中的数据
    """
    queryset = StepModel.objects.all()
    serializer_class = StepSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)   # 验证访问该API权限，以及如果要通过API删除step，该step是否属于owner

    # 实现上面获取queryset的具体方法，下面的方法是只获取属于该用户的step数据
    def get_queryset(self):
        return StepModel.objects.filter(user=self.request.user)


class StepDataViewSet(viewsets.ViewSet):
    # Required for the Browsable API renderer to have a nice form.
    serializer_class = StepDataSerializer
    permission_classes = (IsAuthenticated, )
    # def list(self, request):
    #     serializer = StepDataSerializer(
    #         instance=StepData.values(), many=True)
    #     return Response(serializer.data)
    '''
    获取对应step的数据
    '''
    def retrieve(self, request, pk=None):
        try:
            step = StepModel.objects.get(id=pk)
        except KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        ES_Data_hits = search("http://192.168.1.84:9200/dy_coalchemical_sxsypp/_search",
                              step.start_date.strftime('%Y-%m-%d'), step.end_date.strftime('%Y-%m-%d'))["hits"]["hits"]
        res = {}
        for i in range(0, len(ES_Data_hits)):
            res[i] = StepData(id=ES_Data_hits[i]["_source"]["id"], date=ES_Data_hits[i]["_source"]["create_at"].split('T')[0],
                              type_name=ES_Data_hits[i]["_source"]["type_name"], value=ES_Data_hits[i]["_source"]["value"])
        # for循环将从elasticsearch获取的数据，转化为stepData对象集合，然后传入serializer进行序列化
        serializer = StepDataSerializer(instance=res.values(), many=True)
        return Response(serializer.data)

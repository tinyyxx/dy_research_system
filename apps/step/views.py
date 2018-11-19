from django.shortcuts import render
from .models import StepModel
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly
from .serializers import StepSerializer

# Create your views here.


class StepViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = StepModel.objects.all()
    serializer_class = StepSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)   # 验证访问该API权限，以及如果要通过API删除step，该step是否属于owner

    # 实现上面获取queryset的具体方法，下面的方法是只获取属于该用户的step数据
    def get_queryset(self):
        return StepModel.objects.filter(user=self.request.user)


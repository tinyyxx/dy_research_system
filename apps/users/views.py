from django.shortcuts import render
from .models import UserProfile
from rest_framework import mixins, viewsets
from .serializers import UserSerializer

# Create your views here.


class UserViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    获取所有用户和字段列表
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

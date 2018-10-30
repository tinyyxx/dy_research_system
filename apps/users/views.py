from django.shortcuts import render
from .models import UserProfile
from rest_framework import mixins, generics, viewsets
from .serializers import UserSerializer

# Create your views here.


class UserViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

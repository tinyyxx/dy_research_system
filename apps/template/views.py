from django.shortcuts import render
from .serializers import TemplateSerializer
from rest_framework import viewsets
from .models import TemplateModel
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly
# Create your views here.


class TemplateViewSet(viewsets.ModelViewSet):

    queryset = TemplateModel.objects.all()
    serializer_class = TemplateSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_queryset(self):
        return TemplateModel.objects.filter(user=self.request.user)

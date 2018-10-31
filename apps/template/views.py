from django.shortcuts import render
from .serializers import TemplateSerializer
from rest_framework import mixins, viewsets
from .models import TemplateModel
# Create your views here.


class TemplateViewSet(viewsets.ModelViewSet):
    queryset = TemplateModel.objects.all()
    serializer_class = TemplateSerializer

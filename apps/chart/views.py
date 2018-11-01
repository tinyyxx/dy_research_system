from django.shortcuts import render
from.serializer import ChartSerializer
from rest_framework import viewsets
from .models import ChartModel

# Create your views here.


class ChartViewSet(viewsets.ModelViewSet):
    queryset = ChartModel.objects.all()
    serializer_class = ChartSerializer

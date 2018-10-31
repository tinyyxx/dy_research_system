from rest_framework import serializers
from .models import ChartModel


class ChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartModel
        fields = "__all__"

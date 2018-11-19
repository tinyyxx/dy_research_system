from rest_framework import serializers
from .models import StepModel


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepModel
        fields = "__all__"

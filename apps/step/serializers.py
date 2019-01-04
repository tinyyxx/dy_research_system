from rest_framework import serializers
from .models import StepModel
from . import StepData


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepModel
        fields = "__all__"


# step 提取数据
class StepDataSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    date = serializers.CharField(max_length=20)
    type_name = serializers.CharField(max_length=30)
    value = serializers.FloatField()

    def create(self, validated_data):
        return StepData(id=None, **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance


from rest_framework import serializers
from template.models import TemplateModel


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateModel
        fields = "__all__"

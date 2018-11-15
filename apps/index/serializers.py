from rest_framework import serializers
from index.models import IndexModel


class IndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndexModel
        fields = "__all__"

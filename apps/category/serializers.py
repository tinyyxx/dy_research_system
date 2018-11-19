from rest_framework import serializers
from .models import CategoryModel

"""
左侧导航栏目录序列化serializer
"""


class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = CategoryModel
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = CategoryModel
        fields = "__all__"


class GetIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ["id", "name", "parent_category"]


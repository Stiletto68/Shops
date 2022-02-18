from rest_framework import serializers
from shops.models import Shop


class ShopsJSONSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    description = serializers.CharField()
    address = serializers.CharField()
    index = serializers.IntegerField()
    is_deleted = serializers.BooleanField()

    class Meta:
        model = Shop
        fields = ['organization', 'name', 'description', 'address', 'index', 'is_deleted']

    def create(self, validated_data):
        return Shop.objects.create(**validated_data)

    depth = 1


class OptionShopSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    description = serializers.CharField()
    address = serializers.CharField()
    index = serializers.IntegerField()

    class Meta:
        model = Shop
        fields = ['name', 'description', 'address', 'index']

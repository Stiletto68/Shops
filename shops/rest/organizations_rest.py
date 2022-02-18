from rest_framework import serializers
from shops.models import Organization
from shops.rest.shops_rest import OptionShopSerializer


class OrganizationJSONSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    description = serializers.CharField()
    shops = OptionShopSerializer(many=True, read_only=True)

    class Meta:
        model = Organization
        fields = ('name',
                  'description',
                  'shops')

    def create(self, validated_data):
        return Organization.objects.create(**validated_data)

    depth = 1

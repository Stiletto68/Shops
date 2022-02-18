from rest_framework import serializers
from shops.models import Organization, Shop
from shops.rest.shops_rest import OptionShopSerializer


class OrganizationJSONSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField()
    description = serializers.CharField()
    shops = OptionShopSerializer(many=True, read_only=True)

    class Meta:
        model = Shop
        fields = ('name',
                  'description',
                  'shops')
        depth = 1

    def create(self, validated_data):
        shops_data = validated_data.pop('shops')
        organization = Organization.objects.create(**validated_data)
        for shop_data in shops_data:
            Shop.objects.create(organizatioin=organization, **shop_data)
        return organization

    depth = 1

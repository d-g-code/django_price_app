from rest_framework import serializers
from .models import Store, Kind, Product


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('store',)


class KindSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kind
        fields = ('kind',)


class ProductSerializer(serializers.ModelSerializer):
    product_kind = serializers.CharField()
    product_store = serializers.CharField()

    class Meta:
        model = Product
        fields = ('product', 'price', 'product_kind', 'product_store')

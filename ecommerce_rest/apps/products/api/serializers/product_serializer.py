from apps.products.models import Product
# from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):

    # 3 methods to work with foreign keys in source model

    # # A read only field that represents its targets using their plain string representation.
    # measure_unit = serializers.StringRelatedField()  # Metodo 2
    # # This method brings all the information from the other serializer
    # category_product = CategoryProductSerializer()  # Metodo 1

    class Meta:
        model = Product
        exclude = ('state',)

    # Method 3
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'image': instance.image if instance.image != '' else '',
            'measure_unit': instance.measure_unit.description,
            'category_product': instance.category_product.description
        }

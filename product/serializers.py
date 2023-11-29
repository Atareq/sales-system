from rest_framework import serializers
from .models import Product
from rest_framework import status
from rest_framework.response import Response
class ProductSerializer(serializers.ModelSerializer):
    
  
    class Meta:
        model = Product
        fields = [
            "name","carton_pieces", "carton_num",
            "carton_price", "peice_price",
            "peice_quentity", 'barcode'
            ]
        extra_kwargs = {
            "product_name": {"required": True},"carton_pieces": {"required": True},
            "carton_num": {"required": True},"carton_price": {"required": True},
            "peice_price": {"required": True},"piece_profit": {"required": True},
            "peice_quentity": {"required": True},'barcode': {"required": False}
        }


# class ProductChangedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductChanged
#         fields = '__all__'

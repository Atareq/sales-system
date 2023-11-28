from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product
from PIL import Image
from pyzbar.pyzbar import decode
from django.db.models import Q

class ProductAPI(APIView):

    def post(self, request):
        try :
            barcode = request.FILES.get('barcode')
            barcode = get_barcode(barcode)
            request.data['barcode'] = barcode
            serializer = ProductSerializer(data=request.data)
   
        except:
            serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        barcode = request.FILES.get('barcode')
        if not barcode:
            return Response({'message': ' you did not provide barcode'}, status=status.HTTP_204_NO_CONTENT)
        try:

            decoded_text = get_barcode(barcode)
            # check if this product quentity and if it is 0 we del the object
            # and search for another product with the same barcode and check that also
            # and if we couldnot find another product we send that Response  
            product = Product.objects.filter(barcode=decoded_text).first()
            while product.peice_quentity == 0:
                product.objects.delete()
                try:
                    product = Product.objects.filter(barcode=decoded_text).first()
                except:
                    return Response({'message': 'Out of stock'}, status=status.HTTP_200_OK)
            return Response({'Product id': product.id, 'Product name': product.name,}, status=status.HTTP_200_OK)
        except:
            return Response({'message': ' invalid barcode '}, status=status.HTTP_204_NO_CONTENT)

      
def get_barcode(barcode):
    pil_image = Image.open(barcode)
    decoded_objects = decode(pil_image)
    decoded_text = decoded_objects[0].data.decode('utf-8')
    return decoded_text
    
# Uncomment and modify if you have specific functionality to register at exit
# atexit.register(your_exit_function)

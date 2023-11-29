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
        try:
            # Extract barcode from the uploaded file
            barcode_file = request.FILES.get('barcode')
            barcode = get_barcode(barcode_file)
            request.data['barcode'] = barcode
            serializer = ProductSerializer(data=request.data)
        except:
            serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            # Calculate and set piece_profit before saving the product
            product = serializer.save()
            product.piece_profit = product.peice_price - (product.carton_price / product.carton_pieces)
            product.save()

            # Return a successful response with product profit and ID
            return Response({'product profit': product.piece_profit, 'product id': product.id}, status=status.HTTP_201_CREATED)
        
        # Return validation errors if the serializer is not valid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        # id = request.data.get('id')
        # print (id)
        # product = Product.objects.get(id= id)
        # return Response({'Product id': product.id, 'Product carton quentity': product.carton_num,'Product peice quentity': product.peice_quentity,'peices in single cartoon':product.carton_pieces}, status=status.HTTP_200_OK)

        barcode_file = request.FILES.get('barcode')

        if not barcode_file:
            # Return a response if barcode is not provided
            return Response({'message': 'You did not provide a barcode'}, status=status.HTTP_204_NO_CONTENT)

        try:
            # Decode the barcode and query for the product
            decoded_text = get_barcode(barcode_file)
            product = Product.objects.filter(Q(barcode=decoded_text) & Q(peice_quentity__gt=0)).first()

            # Return product information if found
            return Response({
                'Product id': product.id,
                'Product name': product.name,
                'Product carton quantity': product.carton_num,
                'Product piece quantity': product.peice_quentity,
                'Pieces in single carton': product.carton_pieces
            }, status=status.HTTP_200_OK)

        except:
            # Return a response if barcode is invalid or product is out of stock
            return Response({'message': 'Invalid barcode or out of stock'}, status=status.HTTP_204_NO_CONTENT)

def get_barcode(barcode):
    # Open the barcode image and decode
    pil_image = Image.open(barcode)
    decoded_objects = decode(pil_image)
    decoded_text = decoded_objects[0].data.decode('utf-8')
    return decoded_text

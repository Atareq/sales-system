from django.shortcuts import render
from rest_framework.views import APIView
from.models import TraderReceipt
from rest_framework.response import Response  
from rest_framework import status
from rest_framework.authtoken.models import Token
from receipt_product.models import CustomerReceiptProduct ,TraderReceiptProduct
from product.models import Product
from product.API import get_barcode
class TraderReceiptAPI(APIView):
    def post(self, request):
            user = request.user
            receipt = TraderReceipt.objects.create(creator=user)           
            orders_data = request.data.get('orders', [])
            total_price = 0
            for i in orders_data:
                item_id = i['item_id']
                item_receipt=TraderReceiptProduct.objects.get(id=item_id)
                item_receipt.receipt=receipt
                item_receipt.cartons = i['carton_number']
                item_receipt.peices = i['pieces_number']
                product =  item_receipt.product
                carton_price = product.carton_price
                piece_price = product.peice_price
                total_price  += (item_receipt.cartons*carton_price)+(item_receipt.peices*piece_price)
            receipt.kinds_number = orders_data.length()
            orders_data.append({'total_price': total_price})
            orders_data.append({'receipt_id': receipt.pk})

            receipt.total_price = total_price
            return Response({'orders_data': orders_data}, status=status.HTTP_200_OK)

       
    def get(self, request):
        # receipt_id = request.data.get('receipt_id')
        barcode = request.data.get('barcode')
        # print(receipt_id)
        # if receipt_id:
        #     receipt = TraderReceipt.objects.get(id=receipt_id)
        # else:
        #     receipt = TraderReceipt.objects.create(creator=user)

        product = get_barcode(barcode)

        if product is not None:
            item_receipt = TraderReceiptProduct.objects.create(product = product )
            # creating bridge table for the receipt
            data = {'Item id': item_receipt.id,'Item buying price':product.peice_price-product.piece_profit,
                    'carton buying price':product.carton_price,
                    'pieces in carton':product.carton_pieces}
            return Response(data, status=status.HTTP_201_CREATED)

        return Response({'message': 'Barcode not found or invalid'}, status=status.HTTP_400_BAD_REQUEST)
# (Buying case)
def product_changed_amount(request,item_id,new_amount):
    item = TraderReceiptProduct.objects.get(id=item_id)
    item.peices = new_amount

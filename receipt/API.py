from django.shortcuts import render
from rest_framework.views import APIView
from.models import TraderReceipt
from rest_framework.response import Response  
from rest_framework import status
from receipt_product.models import CustomerReceiptProduct ,TraderReceiptProduct
from product.models import Product
from product.API import get_barcode
class TraderReceiptAPI(APIView):
    def post(self, request):
        user = request.user
        receipt = TraderReceipt.objects.create(creator=user)           
        orders_data = request.data.get('orders', [])
        total_price = 0
        
        for i in  orders_data :
            product = Product.objects.get(id=i['product_id'])
            item_receipt=TraderReceiptProduct.objects.create(receipt=receipt,product = product, cartons = i['carton_number'],
            peices = i['pieces_number'])
            # update product cartoons number and peices
            product.carton_num += item_receipt.cartons
            product.peice_quentity += ((item_receipt.cartons*product.carton_pieces)
                                       +item_receipt.peices)
            product.save()
            #extracting the prices from the product to calculate the total value of receipt
            item_receipt.total_price  = ((item_receipt.cartons*product.carton_price)+
                                (item_receipt.peices*(product.peice_price-product.piece_profit)))
            total_price += item_receipt.total_price
        receipt.kinds_number = len(orders_data)
        receipt.total_price = total_price
        orders_data.append({'total_price': total_price})
        orders_data.append({'receipt_id': receipt.pk})

        return Response({'orders_data': orders_data}, status=status.HTTP_200_OK)

       
    def get(self, request):
        barcode = request.data.get('barcode')       
        decoded_text = get_barcode(barcode)
        try:
            product = Product.objects.filter(barcode=decoded_text).first()
            if product is not None:
                item_receipt = TraderReceiptProduct.objects.create(product = product )
                # creating bridge table for the receipt
                data = {'Product name':product.name,'Item buying price':product.peice_price-product.piece_profit,
                        'carton buying price':product.carton_price,
                        'pieces in carton':product.carton_pieces}
                return Response(data, status=status.HTTP_201_CREATED)
        except:
            return Response({'message': 'Barcode not or invalid'}, status=status.HTTP_400_BAD_REQUEST)


# (Buying case)
def product_changed_amount(request,item_id,new_amount):
    item = TraderReceiptProduct.objects.get(id=item_id)
    item.peices = new_amount

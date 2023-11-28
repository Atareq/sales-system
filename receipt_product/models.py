from django.db import models
from receipt.models import CustomerReceipt ,TraderReceipt
from product.models import Product

class CustomerReceiptProduct(models.Model):
    receipt =  models.ForeignKey(CustomerReceipt, on_delete=models.CASCADE)     
    # because on cancelling the receipt i want to delete the changes 
    # on the product and not saving any unnessecery data
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    # i will acess the product using its barcode and not in need for saving the pk
    peices = models.IntegerField(null = True,default=1)
    cartons = models.IntegerField(null=True)
    profit_of_piece = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    # i will search using barcode in the product  and the fields 
    # retrived that i want i will save it inside a product changed class for 
    # better storage utilization and performance
    total_price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    # "barcode"->get"product(pk)"-> minus the quentity ->
    # save the "profit of piece" ->save the (fk)-> signal(after save) ->
    # minas the quentity from the product table

class TraderReceiptProduct(models.Model):
    receipt =  models.ForeignKey(TraderReceipt, on_delete=models.CASCADE,null=True)     
    # because on cancelling the receipt i want to delete the changes 
    # on the product and not saving any unnessecery data
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    product_price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    # i will acess the product using its barcode and not in need for saving the pk
    peices = models.IntegerField(null = True,default=1)
    cartons = models.IntegerField(null=True)
    profit_of_piece = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    #(selling condition)
    # i will search using barcode in the product  and the fields 
    # retrived that i want i will save it inside a product changed class for 
    # better storage utilization and performance
    total_price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    # "barcode"->get"product(pk)"-> minus the quentity ->
    # save the "profit of piece" ->save the (fk)-> signal(after save) ->
    # minas the quentity from the product table
    new_field = models.CharField(max_length=100,null=True)




# class CustomerReceiptChanged(models.Model):
#     receipt =  models.ForeignKey(receipt, on_delete=models.CASCADE)     
#     # because on cancelling the receipt i want to delete the changes 
#     # on the product and not saving any unnessecery data
    
#     product_fk =  models.ForeignKey(Product, on_delete=models.CASCADE)     
#     # i will acess the product using its barcode then i will save its 
#     # pk in this table and then 
#     # barcode = models.CharField(max_length=128, unique=True, blank=True, null=True)
#     # i think i should delete the barcode field and search inside the 
#     # product using its barcode and then save it inside the ProductChanged table
#     quentity_in_piece = models.IntegerField()
#     profit_of_piece = models.DecimalField(max_digits=10, decimal_places=2)
#     # i will search using barcode in the product  and the fields 
#     # retrived that i want i will save it inside a product changed class for 
#     # better storage utilization and performance
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     added_cartons = models.IntegerField()
#     # "barcode"->get"product(pk)"-> minus the quentity ->
#     # save the "profit of piece" ->save the (fk)-> signal(after save) ->
#     # minas the quentity from the product table
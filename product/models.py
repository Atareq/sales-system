import random ,os , pathlib
from barcode import EAN13
from barcode.writer import ImageWriter
from io import BytesIO
from django.db import models
from django.core.files import File
from rest_framework.response import Response
from rest_framework import status
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from sales_system.settings import MEDIA_URL
from pyzbar.pyzbar import decode


class Product(models.Model):
    name = models.CharField(max_length=100)
    carton_pieces = models.IntegerField()
    carton_num = models.IntegerField()
    carton_price = models.DecimalField(max_digits=10, decimal_places=2)
    peice_price = models.DecimalField(max_digits=10, decimal_places=2) 
    #the price of peice after adding the profit
    piece_profit = models.DecimalField(max_digits=10, decimal_places=2)
    peice_quentity = models.IntegerField()
    barcode = models.CharField(max_length=14, unique=False)
    date_intiated =  models.DateTimeField(auto_now_add=True)


# for the condition of generating a barcode if the product doesnot have
    def save(self, *args, **kwargs):
        if not self.barcode:
            
            barcode, buffer = encode_barcode(generate_random())
            decoded_text = decode_barcode(buffer)
            while Product.objects.filter(barcode=decoded_text).exists():
                barcode, buffer = encode_barcode(generate_random())
                decoded_text = decode_barcode(barcode, buffer)
            #due to the problem that the number fiier in the encoding from the decoding so i 
            #save the decoded number in the barcode field and i check if it is duplicated with 
            # another product

            save_barcode(self, decoded_text, barcode)
            self.barcode = decoded_text
        super().save(*args, **kwargs)

def generate_random():
    number = str(random.randint(10**12, (10**13)-1))

    return number 
def encode_barcode(number):
    barcode = EAN13(number, writer=ImageWriter())
    print(number)
    buffer = BytesIO()
    barcode.write(buffer)
    buffer.seek(0)  
    return barcode, buffer

    #buffer turns binary data into a file by saving it in the memory(RAM)
    #so i can decode it as a file


def decode_barcode( buffer):
    decoded_objects = decode(Image.open(buffer))
    if decoded_objects:
        decoded_text = decoded_objects[0].data.decode('utf-8')
        print(decoded_text)
    return decoded_text


def save_barcode(self,decoded_text,barcode):
    filename_with_png = f'barcode_{self.name}.png'
    filename = f'barcode_{self.name}'
        
    destination_path_with_png = os.path.join(MEDIA_URL, filename_with_png)
    destination_path = os.path.join(MEDIA_URL, filename)

    text = decoded_text + '\n' + self.name 
    print(f'destination_path = {destination_path_with_png}')
    counter = 0
    while pathlib.Path(destination_path_with_png).is_file():                   
        counter += 1
        filename_with_png = f'barcode_{self.name}{counter}.png'
        filename= f'barcode_{self.name}({counter})'
        destination_path_with_png = os.path.join(MEDIA_URL, filename_with_png)
        destination_path = os.path.join(MEDIA_URL, filename)
    barcode.save(destination_path, text=text)

           


import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
from django.db.models.signals import post_save
from django.dispatch import receiver
from product.models import Product
import random
import string

@receiver(post_save, sender=Product)
def generate_and_save_barcode(sender, instance, **kwargs):
    if not instance.barcode: 
        product_id = str(instance.id).zfill(12)  # Ensure product ID is 12 digits
        ean = barcode.get_barcode_class('ean13')(product_id, writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        instance.barcode.save(f'barcode_{instance.id}.png', File(buffer), save=True)
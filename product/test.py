from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from product.models import Product

class ProductSaveTestCase(TestCase):
    def test_save_method_generates_barcode(self):
        # Create an instance of the Product model with no barcode
        product = Product(
            name="Test Product",
            carton_pieces=10,
            carton_num=5,
            carton_price=50.00,
            peice_price=10.00,
            piece_profit=5.00,
            peice_quentity=100,
        )

        # Save the instance to trigger the save method
        product.save()

        # Ensure that a barcode has been generated and saved
        self.assertIsNotNone(product.barcode)

    def test_save_method_does_not_generate_duplicate_barcodes(self):
        # Create an instance of the Product model with a barcode
        product_with_barcode = Product(
            name="Test Product",
            carton_pieces=10,
            carton_num=5,
            carton_price=50.00,
            peice_price=10.00,
            piece_profit=5.00,
            peice_quentity=100,
        )
        product_with_barcode.barcode = "123456789012"  # Replace with a valid barcode

        # Save the instance to trigger the save method
        product_with_barcode.save()

        # Create another instance with the same barcode
        product_with_duplicate_barcode = Product(
            name="Another Product",
            carton_pieces=10,
            carton_num=5,
            carton_price=50.00,
            peice_price=10.00,
            piece_profit=5.00,
            peice_quentity=100,
        )
        product_with_duplicate_barcode.barcode = "123456789012"  # Use the same barcode

        # Save the instance, which should not generate a duplicate barcode
        product_with_duplicate_barcode.save()

        # Ensure that the barcodes are not equal (i.e., not duplicates)
        self.assertNotEqual(
            product_with_barcode.barcode,
            product_with_duplicate_barcode.barcode
        )

from django.core.management.base import BaseCommand
from search.models import ProductData
from search.loader import Loader

class Command(BaseCommand):
    help = "Load products in postgres DB"

    def handle(self, *args, **options):
        loader = Loader()

        raw = loader.df_raw_index_sku 
        for sku, product in raw.items():
            ProductData.objects.get_or_create(
                product_name=product["name"],
                product_sku=sku,
                product_description=product["description"], 
                product_category=product["category"],
                product_price=product["price"],
                product_image=product["image"],
                product_currency=product["currency"],
                product_url=product["url"],
                product_brand="",
                product_is_available=product["availability"],
                product_is_active=True,
            )



from django.core.management.base import BaseCommand
from search.models import ProductEmbedding, ProductData
from search.loader import Loader

class Command(BaseCommand):
    help = 'Load embeddings into DB'

    def handle(self, *args, **kwargs):
        loader = Loader()

        embeddings = loader.df_stacked_data

        for _, row in embeddings.iterrows():
            try:
                product = ProductData.objects.get(product_sku=row["sku"])
            except ProductData.DoesNotExist:
                continue
             
            ProductEmbedding.objects.get_or_create(
            embedding_source_type = row["source_type"],
            product_source= product,
            
            embedding_source_text = row["source_text"],
            embedding_vector = row["source_embeddings"],
            )
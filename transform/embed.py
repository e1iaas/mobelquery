
def create_embeddings(product_name, product_description, model):
    print("=== CREATING EMBEDDINGS ===")
   
    product_name_embeddings = model.encode(
        product_name,
        convert_to_numpy=True
    )
    product_description_embeddings = model.encode(
        product_description,
        convert_to_numpy=True
    )

    print(f"\n Created embeddings!")


    return product_name_embeddings, product_description_embeddings


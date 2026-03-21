from transform.regex_clean import pre_process_regex, post_process_regex, chunk_text
from transform.semantic.semantic_spacy import run_semantic_score

#FULL SEMANTIC SCRORE FUNCTION with prefiltering chunking and final scroing filter use for bad product description data


#INPUT list OUTPUT list
results = []
all_rows = []
final_rows = []
def chunk_and_score(raw_product_description):  

     #clean raw description
    pre_description_regex = pre_process_regex(raw_product_description)
    post_description_regex = post_process_regex(pre_description_regex)
    chunked_text = chunk_text(post_description_regex)

            

    for chunk in chunked_text:
        score,reasons = run_semantic_score(chunk)

        results.append({
            "chunk": chunk,
            "score": score,
        })

    top_chunks = sorted(results, key=lambda x: x["score"], reverse = True)[:1]

    for c in top_chunks:
        rows = {
            "sku": product.product_sku,
            "chunk_text": c["chunk"],
            "semantic_score": c["score"],

        }
        all_rows.append(rows)

    
    for row in all_rows:
        if row["semantic_score"] < 7:
            continue
    
    final_rows.append({
        "sku": row["sku"],
        "chunk_text": row["chunk_text"],
        "semantic_score": row["semantic_score"],
    })

    return final_rows
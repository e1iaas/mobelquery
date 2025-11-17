import pandas as pd
import re
import spacy
from collections import Counter

def regex_clean(text: str) -> str:
    if not text:
        return ""

    text = re.sub(r"[^a-zA-Z0-9.,'\"\s-]", " ", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"([!?.,])\1+", r"\1", text)  # !! -> !
    return text.strip()

def process_text(whitelist_set: str, blacklist_set: str, text: str, nlp_model) -> str:
    """Clean text using whitelist and blacklist"""
    if not text or pd.isna(text):
        return ""

    doc = nlp_model(str(text))
    kept_tokens = []

    for token in doc:
        if not token.is_alpha:
            continue

        word_lower = token.lemma_.lower()

        # Skip empty tokens
        if not word_lower:
            continue

        # Remove if in blacklist
        if word_lower in blacklist_set:
            continue

            # Keep all other tokens (including stop words and numbers)
        if token.is_alpha or token.like_num:
            kept_tokens.append(word_lower)

    return ' '.join(kept_tokens)  # FIXED: return outside loop

try:
    with open("blacklist.txt", 'r') as f:
        blacklist = {line.strip().lower() for line in f if line.strip()}
    print(f"✓ Loaded {len(blacklist)} words in blacklist")
except FileNotFoundError:
    print("⚠️  blacklist.txt not found, using empty blacklist")
    blacklist = set()







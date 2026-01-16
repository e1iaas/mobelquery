import spacy
import re


nlp = spacy.load("en_core_web_sm", disable=['parser', 'ner'])
nlp.max_length = 2000000
nlp.add_pipe('sentencizer')


def pre_process_regex(text: str):
    if not isinstance(text, str):
        return ""

    text = re.sub(r'\b(Product|Category|Description|Price Category|Features|Specifications):\s*', '', text, flags=re.IGNORECASE)

    # Normalize newlines
    text = text.replace("\n", ". ")

    # Fix hyphen punctuation
    text = re.sub(r"\s-\s", ". ", text)

    # Add space after periods if missing
    text = re.sub(r"\.(?=[A-Za-z0-9])", ". ", text)

    # Fix duplicate periods
    text = re.sub(r'\.{2,}', '.', text)

    # Fix multiple spaces
    text = re.sub(r"\s{2,}", " ", text)

    return text.strip()



def post_process_regex(text: str):
    text = re.sub(r"(?<=\b[a-zA-Z])\s*,\s*(?=[a-zA-Z])", ". ", text)
    return text.lower().strip()


def chunk_text(text):
    if not isinstance(text, str) or not text.strip():
        return []

    pre = pre_process_regex(text)
    clean = post_process_regex(pre)
    doc = nlp(clean)
    return [sent.text.strip() for sent in doc.sents if sent.text.strip()]



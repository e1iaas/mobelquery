import spacy
from spacy.matcher import DependencyMatcher, Matcher
from .semantic_patterns import patterns, SCORES, pm_high_value_np, domain_noun_list, CORE_DOMAIN_NOUNS
from .semantic_word_list import (FLUFF_NOUNS, MATERIAL_ADJ, MATERIAL_NOUNS, STRUCTURAL_ADJ, FLUFF_ADJ,
                                QUALITY_CLAIMS, PERFORMANCE_CLAIMS, COMFORT_CLAIMS, CLEANING_LEMMAS, LOGISTICS_WORDS,
                                DIMENSION_WORDS, DIMENSION_REGEX, COLORS)
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
file_path = BASE_DIR /"etl"/ "data" / "raw" /"sentence_split_preview.json"

nlp = spacy.load("en_core_web_sm")

token_matcher = Matcher(nlp.vocab)
matcher = DependencyMatcher(nlp.vocab)


matcher.add("SEMANTIC_CORE", patterns)
token_matcher.add("HIGH_VALUE_NP", [pm_high_value_np])


def count_verbs(doc):
    #count verbs, indicate, marketing fluff

    verb_count = 0

    for token in doc:
    # VBZ, VBP, VBD = finite verbs (is, are, was, etc.)
    # Skip VBN, VBG when used as adjective

        if token.tag_ in ["VBZ", "VBP", "VBD", "VB", "MD"]:
            verb_count += 1
        elif token.tag_ in ["VBG", "VBN"]:
            #only count if actually verb and not adjective
            if token.dep_ not in ["amod", "compound"]:
                verb_count += 1

    return verb_count


def score_noun_phrases(doc):
    score = 0
    reasons = []
    has_scored_domain = False

    for chunk in doc.noun_chunks:
        has_domain = any(t.pos_ in ("NOUN", "PROPN") and t.lemma_.lower() in domain_noun_list for t in chunk)

        if not has_domain:
            continue

        if not  has_scored_domain:
            has_scored_domain = True
            score += 5
            reasons.append("has domain noun")


        #score modifiers (adj and compounds)
        modifier_count = sum(1 for t in chunk if t.lemma_.lower() in MATERIAL_ADJ or t.text.lower() in MATERIAL_NOUNS)

        structual_count = sum(1 for t in chunk if t.lemma_.lower() in STRUCTURAL_ADJ)

        colors_count = sum(1 for t in chunk if t.lemma_.lower() in COLORS)

        modifier_structual_count = modifier_count + structual_count + colors_count

        if modifier_structual_count >= 1:
            score += modifier_structual_count * 2
            reasons.append(f"modifier bonus count: {modifier_structual_count}")

    return score, reasons



def count_fluff(doc):
    # penzlie words and phrases
    score = 0
    reasons = []

    fluff_nouns = sum(1 for t in doc if t.lemma_.lower() in FLUFF_NOUNS)
    fluff_adj = sum(1 for t in doc if t.lemma_.lower() in FLUFF_ADJ)

    fluff_logi_clean = sum(1 for t in doc if t.lemma_.lower() in LOGISTICS_WORDS | CLEANING_LEMMAS | DIMENSION_WORDS)
    fluff_quality_claims = sum(
        1 for t in doc if t.lemma_.lower() in QUALITY_CLAIMS | PERFORMANCE_CLAIMS | COMFORT_CLAIMS)

    if fluff_nouns > 0:
        score -= fluff_nouns * 4
        reasons.append(f"fluff noun count:{fluff_nouns}")

    if fluff_adj > 0:
        score -= fluff_adj * 4
        reasons.append(f"fluff adj count:{fluff_adj}")

    if fluff_logi_clean > 0:
        score -= fluff_logi_clean * 8
        reasons.append(f"fluff logi count:{fluff_logi_clean}")

    if fluff_quality_claims > 0:
        score -= fluff_quality_claims * 8
        reasons.append(f"fluff quality claim count:{fluff_quality_claims}")

    return score, reasons


def score_sentence_length(sentence_length, max_dep_len):
    """
    takes inputs:
    -len(doc) as input(sentence_length
    -len(dependacy_matcher) as max_dep_len
    """
    score = 0
    reasons = []

    if 6 <= max_dep_len <= 8:
        score += SCORES["long_token"]
        reasons.append("long dep match")

    if max_dep_len >= 9:
        score += SCORES["too_long_token"]
        reasons.append("too long dep match")

    if 15 < sentence_length <= 31:
        score += SCORES["long_token"]
        reasons.append("long sentence match")

    if sentence_length > 32:
        score += SCORES["too_long_token"]
        reasons.append("too long sentence match")

    return score, reasons

def semantic_score(text,doc, dep_matches, token_matches):
    score = 0
    reasons = []


    if dep_matches and any(t.lemma_.lower() in CORE_DOMAIN_NOUNS for t in doc ):
        score += SCORES["dep_matches"]
        reasons.append("dependancy_pattern")

    max_dep_len = max((len(m[1]) for m in dep_matches), default = 0)
    sentence_length = len(doc)

    length_score, length_reasons = score_sentence_length(sentence_length, max_dep_len)
    score += length_score
    reasons.extend(length_reasons)

    if token_matches and any(t.lemma_.lower() in CORE_DOMAIN_NOUNS for t in doc):
        score += SCORES["token_matches"]
        reasons.append("token_pattern")

    if 0 < sentence_length <= 5 and token_matches:
        score += SCORES["short_phrase_bonus"]
        reasons.append("short high-value phrase")

    noun_score, noun_reasons = score_noun_phrases(doc)
    score += noun_score
    reasons.extend(noun_reasons)


    verb_count = count_verbs(doc)

    if verb_count > 0:
        score += SCORES["verb_penalty"] * verb_count
        reasons.append(f"contains {verb_count} verbs")

    fluff_score, fluff_reasons = count_fluff(doc)
    score += fluff_score
    reasons.extend(fluff_reasons)

    if DIMENSION_REGEX.search(text):
        score += SCORES["dimension_penalty"]
        reasons.append("dimensions content")


    return score, reasons


#return top 4 highest scoring sentencses for each description

def run_semantic_score(text):
    doc = nlp(text)

    dep_matches = matcher(doc)
    token_matches = token_matcher(doc)

    score, reasons = semantic_score(
    text,
    doc,
    dep_matches,
    token_matches
    )

    return score, reasons


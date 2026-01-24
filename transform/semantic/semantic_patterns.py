#Scores for semantic scoring


SCORES = {
    "dep_matches": 3,
    "token_matches": 2,

    "material_adj": 4,
    "short_phrase_bonus": 3,

    "verb_penalty": -8,
    "cleaning_penalty": -20,
    "logistics_penalty": -20,
    "dimension_penalty": -20,
    "fluff_noun": -3,
    "fluff_adj": -3,

    "long_token": -3,
    "too_long_token": -10
}

CORE_DOMAIN_NOUNS = {
    "sofa", "couch", "loveseat", "chair", "table",
    "frame", "top", "cabinet", "dresser", "bed",
    "mattress", "ottoman", "sectional", "shelf"
}

#should be to match atleast one head noun
domain_noun_list = [
    "chair", "armchair", "sofa", "couch", "loveseat",
    "bench", "stool", "ottoman", "chaise", "recliner", "seat",
    "bed", "bedframe", "frame", "headboard", "footboard", "mattress",
    "daybed", "bunk", "crib",
    "table", "desk", "console", "counter",
    "nightstand", "dresser", "vanity",
    "cabinet", "cupboard", "wardrobe", "closet",
    "shelf", "shelving", "bookcase",
    "drawer", "chest", "sideboard", "buffet",
    "lounge", "settee", "sectional", "stand"
]

#High-value noun phrase matcher
pm_high_value_np = [
    {"POS": {"IN": ["NOUN","PROPN"]}, "LEMMA": {"IN": domain_noun_list}}]

pattern_high_value_np = [
    {
        "RIGHT_ID": "head",
        "RIGHT_ATTRS": {"POS": {"IN": ["PROPN", "NOUN"]}}
    },
    {
        "LEFT_ID": "head",
        "REL_OP": "<",
        "RIGHT_ID": "mod_1",
        "RIGHT_ATTRS": {
            "DEP": {"IN": ["amod", "compound", "appos" ]},
            "POS": {"IN": ["ADJ", "PROPN", "NOUN"]}
        }
    },
    {
        "LEFT_ID": "mod_1",
        "REL_OP": "<",
        "RIGHT_ID": "mod_2",
        "RIGHT_ATTRS": {
            "DEP": {"IN": ["amod", "compound", "appos" ]},
            "POS": {"IN": ["ADJ", "PROPN", "NOUN"]}
        }
    },
    {
        "LEFT_ID": "mod_2",
        "REL_OP": "<",
        "RIGHT_ID": "mod_3",
        "RIGHT_ATTRS": {
            "DEP": {"IN": ["amod", "compound", "appos" ]},
            "POS": {"IN": ["ADJ", "PROPN", "NOUN"]}
        }
    }
]

# PATTERNS FOR SPACY DEPENDANCY MATCHER
pattern_adj_noun = [
    {
        "RIGHT_ID": "noun",
        "RIGHT_ATTRS": { "POS": "NOUN"}
    },
    {
        "LEFT_ID": "noun",
        "REL_OP": "<",
        "RIGHT_ID": "adj",
        "RIGHT_ATTRS": {"DEP": "amod"}
    }
]


pattern_adj_noun_flexible = [
    {
        "RIGHT_ID": "head",
        "RIGHT_ATTRS": {"POS": {"IN": ["NOUN", "PROPN"]}}
    },
    {
        "LEFT_ID": "head",
        "REL_OP": "<",
        "RIGHT_ID": "mod_1",
        "RIGHT_ATTRS": {"DEP": {"IN": ["amod", "compound"]}, "POS": {"IN": ["ADJ","PROPN","NOUN", "VERB"]}}
    },
    {
        "LEFT_ID": "mod_1",
        "REL_OP": "<",
        "RIGHT_ID": "mod_2",
        "RIGHT_ATTRS": {"DEP": {"IN": ["amod", "compound"]}, "POS": {"IN": ["ADJ", "PROPN", "NOUN", "VERB"]}}
    }
]


pattern_feature_with_material = [
    {
        "RIGHT_ID": "feature",
        "RIGHT_ATTRS": {"POS": "NOUN"}
    },
    {
        "LEFT_ID": "feature",
        "REL_OP": ">",
        "RIGHT_ID": "prep",
        "RIGHT_ATTRS": {"DEP": "prep", "LEMMA": "with"}
    },
    {
        "LEFT_ID": "prep",
        "REL_OP": ">",
        "RIGHT_ID": "material",
        "RIGHT_ATTRS": {"DEP": "pobj", "POS": "NOUN"}
    }
]

pattern_compound_noun = [
    {
        "RIGHT_ID": "head",
        "RIGHT_ATTRS": {"POS": "NOUN"}
    },
    {
        "LEFT_ID": "head",
        "REL_OP": "<",
        "RIGHT_ID": "modifier",
        "RIGHT_ATTRS": {"DEP": "compound"}
    }
]

pattern_noun_material = [
    {
        "RIGHT_ID": "head",
        "RIGHT_ATTRS": {"POS": "NOUN"}
    },
    {
        "LEFT_ID": "head",
        "REL_OP": ">",
        "RIGHT_ID": "prep",
        "RIGHT_ATTRS": {"DEP": {"IN": ["prep", "acl"]}, "LEMMA": {"IN": ["of", "make", "construct", "craft"]}}
    },
    {
        "LEFT_ID": "prep",
        "REL_OP": ">",
        "RIGHT_ID": "material",
        "RIGHT_ATTRS": {"DEP": "pobj", "POS": "NOUN"}
    }
]

pattern_multi_compound = [
    {
        "RIGHT_ID": "head",
        "RIGHT_ATTRS": {"POS": "NOUN"}
    },
    {
         "LEFT_ID": "head",
         "REL_OP": "<",
         "RIGHT_ID": "modif_1",
         "RIGHT_ATTRS": {"DEP": "compound"}
    },
    {
        "LEFT_ID": "modif_1",
        "REL_OP": "<",
        "RIGHT_ID": "modif_2",
        "RIGHT_ATTRS": {"DEP": "compound", "POS": "NOUN"}
    }
]

patterns = [pattern_high_value_np, pattern_adj_noun, pattern_feature_with_material, pattern_compound_noun, pattern_noun_material, pattern_multi_compound, pattern_adj_noun_flexible]
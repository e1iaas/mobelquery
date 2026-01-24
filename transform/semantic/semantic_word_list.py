import re

DIMENSION_REGEX = re.compile(r"\d+(\.d+)?\s*(\"|in|cm|mm|ft|''|width)", re.IGNORECASE)

MATERIAL_ADJ = {
    "wooden", "metal", "metallic", "leather",
    "fabric", "linen", "velvet", "feather", "faux",
    "synthetic", "oak", "walnut", "pine", "wool",
    "wood", "feather", "steel", "velvet"
}

# Material nouns (for compound matching)
MATERIAL_NOUNS = {
    "wood", "oak", "walnut", "pine", "metal", "steel",
    "leather", "fabric", "velvet", "linen", "cotton",
    "foam", "feather", "fiber", "down"
}


# Structural/functional terms (GOOD modifiers)
STRUCTURAL_ADJ = {
    "modular", "sectional", "corner", "reversible",
    "removable", "convertible", "adjustable", "reclining",
    "L-shaped", "U-shaped", "armless", "oversized",
    "storage", "sleeper", "filled", "stuffed", "verstuffed"
}

FLUFF_ADJ = {
    "engineered", "designed", "tested", "certified",
    "luxurious", "comfortable", "premium",  "amazing",
    "clean", "easily", "easy", "effortlessly", "elegant",
    "excellent", "exceptional","fantastic", "great", "high",
    "ideal", "incredible","perfect","perfectly","premium",
    "refined", "simply", "soft", "sophisticated", "superior",
    "timeless", "ultimate", "wonderful", "super", "perfect",
    "sophisticated", "welcome", "cozy", "ultimate"
}

FLUFF_NOUNS = {
    "designed","tested", "minimum", "ultimate", "experience"
    "functionality","comfort","feeling", "clean", "vibes"
    "soft", "easy", "high", "luxurious", "expertly", "relaxation",
    "cozy",  "retro",  "modern", "plump", "decor", "addition",
    "seating", "overall",  "relaxation", "amazing", "beautiful", "stylish"
}


QUALITY_CLAIMS = {
    "sturdy", "durable", "heavy-duty",
    "commercial-grade", "premium", "high-quality"
}

COMFORT_CLAIMS = {
    "comfortable", "plush", "firm", "soft",
    "supportive", "cushioned", "relaxation",
    "cozy", "medium", "snug", "inviting"
}

PERFORMANCE_CLAIMS = {
    "durable", "long-lasting", "resistant",
    "easy-to-clean", "stain-resistant", "capacity"
}


#LOGISITCS / PACKAGNING / diemensions
LOGISTICS_WORDS = {
    "box", "packaging", "door", "shipping", "assembly", "assembled", "dimension"
}

#words relating to cleaning and not semantically useful
CLEANING_LEMMAS = {
    "clean", "wipe", "blot", "wash", "spot", "remove", "vacuum"
}

DIMENSION_WORDS = {
    "cm","mm","ft"," ' ' ","width", " '' ", "inches", "inch", ' "" ', "Weight"
}

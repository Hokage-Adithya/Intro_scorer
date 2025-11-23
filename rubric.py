"""
Rubric configuration for student self-introduction scoring.
Each criterion has: description, keywords, weight, min/max word limits, and semantic template.
"""

RUBRIC = [
    {
        "criterion": "Personal Introduction",
        "description": "Student introduces themselves with name, age, class, and school",
        "keywords": ["name", "myself", "age", "years old", "class", "school", "studying"],
        "semantic_template": "The student clearly states their name, age, class section, and school name",
        "weight": 20,
        "min_words": 10,
        "max_words": 50
    },
    {
        "criterion": "Family Description",
        "description": "Student describes their family members and family size",
        "keywords": ["family", "mother", "father", "brother", "sister", "parents", "members", "people"],
        "semantic_template": "The student talks about their family members and describes who lives with them",
        "weight": 15,
        "min_words": 5,
        "max_words": 40
    },
    {
        "criterion": "Personal Characteristics",
        "description": "Student shares special traits, qualities, or characteristics about themselves or family",
        "keywords": ["special", "thing", "quality", "characteristic", "unique", "kind", "hearted", "soft spoken"],
        "semantic_template": "The student mentions special characteristics, qualities, or unique traits about themselves or their family",
        "weight": 15,
        "min_words": 5,
        "max_words": 40
    },
    {
        "criterion": "Hobbies and Interests",
        "description": "Student mentions activities they enjoy or hobbies they pursue",
        "keywords": ["enjoy", "hobby", "play", "playing", "like", "love", "sport", "cricket", "activity"],
        "semantic_template": "The student describes activities, hobbies, sports, or things they enjoy doing",
        "weight": 15,
        "min_words": 5,
        "max_words": 40
    },
    {
        "criterion": "Fun Facts or Secrets",
        "description": "Student shares interesting, fun, or personal facts about themselves",
        "keywords": ["fun fact", "secret", "don't know", "people don't know", "interesting", "once"],
        "semantic_template": "The student reveals fun facts, secrets, or interesting personal stories about themselves",
        "weight": 10,
        "min_words": 5,
        "max_words": 40
    },
    {
        "criterion": "Academic Interests",
        "description": "Student discusses favorite subjects and explains why they like them",
        "keywords": ["subject", "favorite", "science", "math", "study", "learn", "because", "interesting", "explore"],
        "semantic_template": "The student talks about their favorite school subjects and provides reasons for their interest",
        "weight": 15,
        "min_words": 5,
        "max_words": 50
    },
    {
        "criterion": "Structure and Coherence",
        "description": "The introduction has a clear beginning, middle, and end with logical flow",
        "keywords": ["hello", "everyone", "thank you", "listening", "introduction", "conclusion"],
        "semantic_template": "The introduction is well-structured with a greeting at the start and closing at the end",
        "weight": 10,
        "min_words": 30,
        "max_words": 200
    }
]

def get_rubric():
    """Returns the rubric configuration"""
    return RUBRIC

def get_total_weight():
    """Returns the total weight of all criteria"""
    return sum([criterion["weight"] for criterion in RUBRIC])

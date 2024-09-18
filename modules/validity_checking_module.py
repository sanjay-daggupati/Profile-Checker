import re
from collections import Counter

def detect_overused_phrases(text, common_phrases=None):
    if common_phrases is None:
        common_phrases = ["team player", "hard worker", "results-driven", "excellent communication skills"]

    words = text.split()
    word_pairs = [' '.join(words[i:i+2]) for i in range(len(words)-1)]
    word_triplets = [' '.join(words[i:i+3]) for i in range(len(words)-2)]

    common_phrases_from_resume = Counter(word_pairs + word_triplets).most_common(10)

    overused_expressions = common_phrases + [phrase for phrase, _ in common_phrases_from_resume]
    
    return overused_expressions

def check_conflicting_details(text):
    experience_pattern = re.compile(r'(\d{4})\s*-\s*(\d{4})')
    matches = experience_pattern.findall(text)
    years = [(int(start), int(end)) for start, end in matches]
    
    conflicts = []
    for i, (start1, end1) in enumerate(years):
        for j, (start2, end2) in enumerate(years):
            if i != j and not (end1 < start2 or end2 < start1):
                conflicts.append((start1, end1, start2, end2))
    
    return conflicts

def check_validity(text, existing_cvs, overused_expressions):
    conflicts = check_conflicting_details(text)
    overused_exprs = detect_overused_phrases(text, overused_expressions)
    return {
        "conflicting_details": conflicts,
        "overused_expressions": overused_exprs
    }

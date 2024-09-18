import re
from modules.keyword_analysis_module import calculate_keyword_score

def calculate_experience_score(text, required_experience_years):
    experience_pattern = re.compile(r'(\d+)\s*years?\s*(?:of\s*)?experience', re.IGNORECASE)
    matches = experience_pattern.findall(text)
    experience_years = sum(int(match) for match in matches)
    return min(experience_years / required_experience_years, 1)

def calculate_education_score(text, required_degree):
    degree_pattern = re.compile(r'\b(bachelor|master|phd)\b', re.IGNORECASE)
    matches = degree_pattern.findall(text)
    degree_levels = {'bachelor': 1, 'master': 2, 'phd': 3}
    max_degree = max([degree_levels[degree.lower()] for degree in matches], default=0)
    required_degree_level = degree_levels.get(required_degree.lower(), 0)
    return min(max_degree / required_degree_level, 1)

def calculate_total_score(text, job_keywords, required_experience_years, required_degree):
    keyword_score = calculate_keyword_score(text, job_keywords)
    experience_score = calculate_experience_score(text, required_experience_years)
    education_score = calculate_education_score(text, required_degree)

    total_score = (keyword_score + experience_score + education_score) / 3
    return total_score, {
        "keyword_score": keyword_score,
        "experience_score": experience_score,
        "education_score": education_score
    }

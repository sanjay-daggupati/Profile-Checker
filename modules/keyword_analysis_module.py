import spacy

nlp = spacy.load("en_core_web_sm")

def extract_keywords(text, job_keywords):
    doc = nlp(text.lower())
    extracted_keywords = [token.text for token in doc if token.text in job_keywords]
    return extracted_keywords

def calculate_keyword_score(text, job_keywords):
    keywords_extracted = extract_keywords(text, job_keywords)
    total_keywords = len(job_keywords)
    matched_keywords = len(keywords_extracted)
    return matched_keywords / total_keywords if total_keywords > 0 else 0

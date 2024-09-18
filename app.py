from flask import Flask, request, render_template
import os
from modules.resume_parsing_module import extract_text
from modules.keyword_analysis_module import calculate_keyword_score
from modules.scoring_engine_module import calculate_total_score
from modules.validity_checking_module import detect_overused_phrases, check_validity

app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    job_description = request.form['job_description']
    skills = request.form['skills']
    resume = request.files['resume']

    # Save the uploaded resume
    resume_path = os.path.join(app.config['UPLOAD_FOLDER'], resume.filename)
    resume.save(resume_path)

    # Extract text from resume
    resume_text = extract_text(resume_path)

    # Dynamic overused expressions based on resume content
    overused_expressions = detect_overused_phrases(resume_text)

    # Parse job keywords from form input
    job_keywords = [skill.strip().lower() for skill in skills.split(",")]
    required_experience_years = 5  # Could be passed from frontend
    required_degree = "Bachelor"   # Could be passed from frontend

    existing_cvs = []  # For now, this is empty. Add past CVs to compare if needed.

    # Perform resume analysis
    result = {
        "total_score": calculate_total_score(resume_text, job_keywords, required_experience_years, required_degree),
        "validity_result": check_validity(resume_text, existing_cvs, overused_expressions)
    }

    return f"Analysis Results: {result}"

if __name__ == '__main__':
    app.run(debug=True)

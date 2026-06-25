import os
import re
import time
import google.generativeai as genai
from flask import Flask, request, render_template, redirect
from werkzeug.utils import secure_filename
import PyPDF2
import json

# ---------------- CONFIG ----------------
UPLOAD_FOLDER = 'uploads'

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ---------------- FLASK APP ----------------
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ---------------- AI FUNCTION ----------------
def analyze_resume(text, job_description=None):
    if not os.getenv("GEMINI_API_KEY"):
        raise ValueError("GEMINI_API_KEY not set")

    jd_block = ""
    jd_schema = ""
    if job_description and job_description.strip():
        jd_block = f"\nJob Description:\n{job_description}\n"
        jd_schema = """,
  "jd_match_score": <integer 0-100, how well the resume matches the job description>,
  "matched_keywords": <list of keywords/skills present in both resume and JD>,
  "missing_keywords": <list of important JD keywords missing from the resume>,
  "tailoring_tips": <list of 3-4 specific tips to tailor this resume for this exact role>"""

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""You are an expert AI resume reviewer and ATS specialist.

Return ONLY valid JSON with this exact structure:

{{
  "score": <integer 0-100 representing overall resume quality>,
  "skills": [],
  "missing_skills": [],
  "suggestions": [],
  "sections": {{
    "contact_info": <true or false>,
    "professional_summary": <true or false>,
    "work_experience": <true or false>,
    "education": <true or false>,
    "skills_section": <true or false>,
    "projects": <true or false>,
    "certifications": <true or false>
  }},
  "ats_tips": []{jd_schema}
}}

Rules:
- score: Rate 0-100 based on completeness, clarity, quantified achievements, and impact
- skills: Extract only important technical/professional skills (max 10-15)
- missing_skills: Suggest relevant skills the resume lacks (max 10)
- suggestions: Give 3-5 strong, specific improvement suggestions
- sections: Detect which standard resume sections are present
- ats_tips: Give 3-4 ATS-specific tips to improve keyword matching and formatting
{"- jd_match_score: Score how well the resume matches the provided job description" if jd_block else ""}
{"- matched_keywords: List skills/keywords found in both resume and job description" if jd_block else ""}
{"- missing_keywords: List important job description keywords absent from the resume" if jd_block else ""}
{"- tailoring_tips: Give 3-4 specific tips to tailor this resume for this exact job role" if jd_block else ""}
- Be specific and professional
{jd_block}
Resume:
{text}"""

    # Retry up to 3 times on rate limit errors
    for attempt in range(3):
        try:
            response = model.generate_content(prompt)
            break
        except Exception as e:
            if "429" in str(e) and attempt < 2:
                time.sleep(30)
            else:
                raise

    result = response.text.strip()

    # Strip markdown fences if present
    if result.startswith("```"):
        result = result.replace("```json", "").replace("```", "").strip()

    # Extract the JSON object
    match = re.search(r'\{[\s\S]*\}', result)
    if not match:
        raise ValueError(f"No JSON found in model response. Raw output: {result[:300]}")

    data = json.loads(match.group())

    output = {
        "score": int(data.get("score", 0)),
        "skills": data.get("skills", []),
        "missing_skills": data.get("missing_skills", []),
        "suggestions": data.get("suggestions", []),
        "sections": data.get("sections", {}),
        "ats_tips": data.get("ats_tips", []),
        "has_jd": bool(jd_block),
    }

    if jd_block:
        output["jd_match_score"] = int(data.get("jd_match_score", 0))
        output["matched_keywords"] = data.get("matched_keywords", [])
        output["missing_keywords"] = data.get("missing_keywords", [])
        output["tailoring_tips"] = data.get("tailoring_tips", [])

    return output


# ---------------- ROUTE ----------------
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        if 'resume' not in request.files:
            return redirect(request.url)

        file = request.files['resume']

        if file.filename == '':
            return redirect(request.url)

        if file and file.filename.endswith('.pdf'):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            job_description = request.form.get('job_description', '').strip()
            analysis_results = None
            error_message = None

            try:
                file.save(filepath)

                with open(filepath, 'rb') as f:
                    pdf_reader = PyPDF2.PdfReader(f)
                    text = "".join(
                        page.extract_text()
                        for page in pdf_reader.pages
                        if page.extract_text()
                    )

                if not text.strip():
                    error_message = "Could not extract text from PDF"
                else:
                    analysis_results = analyze_resume(text, job_description)

            except Exception as e:
                error_message = f"Error: {str(e)}"

            finally:
                if os.path.exists(filepath):
                    os.remove(filepath)

            return render_template('index.html', results=analysis_results, error=error_message)

    return render_template('index.html', results=None, error=None)


# ---------------- RUN ----------------
if __name__ == '__main__':
    app.run(debug=True)

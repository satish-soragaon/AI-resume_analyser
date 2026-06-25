# AI Resume Analyzer

An AI-powered resume analysis tool built with Flask and Google Gemini. Upload your PDF resume and get instant feedback, ATS optimization tips, a score, and optional job description matching.

## Features

- **Resume Scoring** — Get an overall score out of 100 based on completeness, clarity, and impact
- **Section Detection** — Checks for Contact Info, Summary, Experience, Education, Skills, Projects, and Certifications
- **Skills Extraction** — Identifies technical and professional skills found in your resume
- **Missing Skills** — Suggests relevant skills you could add
- **Improvement Suggestions** — 3–5 specific, actionable tips to strengthen your resume
- **ATS Optimization** — Tips to help your resume pass Applicant Tracking Systems
- **Job Description Match** — Paste a job description to get a match score, keyword gap analysis, and tailoring tips
- **Glassmorphism UI** — Animated, modern interface with drag-and-drop file upload

## Tech Stack

- **Backend:** Python, Flask
- **AI:** Google Gemini 2.5 Flash
- **PDF Parsing:** PyPDF2
- **Frontend:** HTML, CSS (Glassmorphism), Vanilla JavaScript

## Getting Started

### Prerequisites

- Python 3.8+
- A [Google AI Studio](https://aistudio.google.com) API key

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/satish-soragaon/AI-resume_analyser.git
   cd AI-resume_analyser
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Set your Gemini API key
   ```bash
   # Windows (PowerShell)
   $env:GEMINI_API_KEY = "your_api_key_here"

   # Mac / Linux
   export GEMINI_API_KEY="your_api_key_here"
   ```

4. Run the app
   ```bash
   python app.py
   ```

5. Open your browser at `http://127.0.0.1:5000`

## Usage

1. Click **Choose a PDF file** or drag and drop your resume
2. Optionally expand **Match against a Job Description** and paste a job posting
3. Click **Analyze My Resume**
4. Review your score, skills, suggestions, and ATS tips

## Deployment

This project is ready to deploy on [Render](https://render.com):

1. Push to GitHub
2. Create a new Web Service on Render
3. Set **Start Command** to `gunicorn app:app`
4. Add `GEMINI_API_KEY` as an environment variable
5. Deploy

## Project Structure

```
AI-resume_analyser/
├── app.py               # Flask backend + Gemini AI logic
├── requirements.txt     # Python dependencies
├── Procfile             # Deployment config
├── templates/
│   └── index.html       # Frontend UI
└── static/
    └── style.css        # Glassmorphism styles
```

## License

This project is licensed under the MIT License.

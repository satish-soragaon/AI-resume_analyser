# AI Resume Analyzer

An AI-powered resume analysis tool built with Flask and Google Gemini 2.5 Flash. Upload your resume and get instant feedback, ATS optimization tips, a score out of 100, and optional job description matching.

🔗 **Live Demo:** [https://ai-resume-analyser-xyo4.onrender.com](https://ai-resume-analyser-xyo4.onrender.com)

## Features

- **Resume Scoring** — Overall score out of 100 based on completeness, clarity, and impact
- **Section Detection** — Checks for Contact Info, Summary, Experience, Education, Skills, Projects, and Certifications
- **Skills Extraction** — Identifies technical and professional skills found in your resume
- **Missing Skills** — Suggests relevant skills you could add
- **Improvement Suggestions** — 3–5 specific, actionable tips to strengthen your resume
- **ATS Optimization** — Tips to help your resume pass Applicant Tracking Systems
- **Job Description Match** — Paste a job description to get a match score, keyword gap analysis, and tailoring tips
- **Multi-format Support** — Accepts PDF, DOCX, and TXT files
- **Drag & Drop Upload** — Easy file upload with drag and drop support
- **Dark Dashboard UI** — Animated dark theme with floating orbs and smooth card animations

## Tech Stack

- **Backend:** Python, Flask
- **AI:** Google Gemini 2.5 Flash
- **PDF Parsing:** PyPDF2
- **DOCX Parsing:** python-docx
- **Frontend:** HTML, CSS (dark dashboard theme), Vanilla JavaScript
- **Fonts:** Manrope + Inter
- **Deployment:** Render

## Getting Started

### Prerequisites

- Python 3.8+
- A [Google AI Studio](https://aistudio.google.com) API key (free)

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

   **Windows (PowerShell)**
   ```powershell
   $env:GEMINI_API_KEY = "your_api_key_here"
   ```

   **Mac / Linux**
   ```bash
   export GEMINI_API_KEY="your_api_key_here"
   ```

4. Run the app
   ```bash
   python app.py
   ```

5. Open your browser at `http://127.0.0.1:5000`

## Usage

1. Click **Choose a file** or drag and drop your resume (PDF, DOCX, or TXT)
2. Optionally expand **Match against a Job Description** and paste a job posting
3. Click **Analyze My Resume**
4. Review your score, skills, suggestions, and ATS tips

## API Key Safety

The API key is stored only as an environment variable — it is **never written in any file** and is not visible on GitHub. It is safe.

## Free Tier Limits

This project uses the Gemini 2.5 Flash free tier:

| Limit | Amount |
|-------|--------|
| Requests per minute | 5 RPM |
| Requests per day | 25 RPD |

25 analyses per day is sufficient for personal use.

## Deployment

This project is deployed on [Render](https://render.com) (free tier):

1. Push to GitHub
2. Create a new Web Service on Render
3. Set **Start Command** to `gunicorn app:app`
4. Add `GEMINI_API_KEY` as an environment variable
5. Deploy

> Note: The free instance spins down after inactivity. The first request may take ~50 seconds to load.

## Project Structure

```
AI-resume_analyser/
├── app.py               # Flask backend + Gemini AI logic
├── requirements.txt     # Python dependencies
├── Procfile             # Render deployment config
├── templates/
│   └── index.html       # Frontend UI
└── static/
    └── style.css        # Dark dashboard styles + animations
```

## License

This project is licensed under the MIT License.

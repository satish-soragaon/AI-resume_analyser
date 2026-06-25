# AI Resume Analyzer

An AI-powered resume analysis tool that gives instant feedback on your resume. Upload a PDF, DOCX, or TXT file and get a score out of 100, skill analysis, ATS optimization tips, and improvement suggestions — all powered by Google Gemini AI.

You can also paste a job description to get a match score, missing keywords, and tailoring tips specific to that role.

🔗 **Live Demo:** [https://ai-resume-analyser-xyo4.onrender.com](https://ai-resume-analyser-xyo4.onrender.com)

## Features

- Resume score out of 100
- Skills found & missing skills
- ATS optimization tips
- Section completeness check
- Job description match score & keyword gap analysis
- Supports PDF, DOCX, and TXT formats
- Drag and drop file upload

## Tech Stack

- **Backend:** Python, Flask
- **AI:** Google Gemini 2.5 Flash
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** Render

## Setup

1. Clone the repo and install dependencies
   ```bash
   pip install -r requirements.txt
   ```

2. Set your Gemini API key
   ```bash
   export GEMINI_API_KEY="your_api_key_here"
   ```

3. Run
   ```bash
   python app.py
   ```

## License

MIT

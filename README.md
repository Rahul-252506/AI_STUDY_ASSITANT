# 🤖 AI Study & Productivity Assistant

An AI-powered study assistant developed as part of the Innovation Hacks AI Internship.

The application uses Google's Gemini API to help students understand and revise study material through summarization, explanations, question generation, structured study notes and interactive Q&A.

---

## 🚀 Features

### 📝 Summarization

Converts lengthy study material into concise bullet-point summaries.

### 💡 Explanation

Explains difficult concepts in simple language using examples and analogies where appropriate.

### ❓ Question Generation

Generates 10 questions from the provided study material with varying difficulty levels from easy to hard, along with answers.

### 📚 Study Notes

Converts study material into structured notes containing key concepts, definitions, examples and important exam points.

### 🔍 Ask Questions

Allows users to ask questions about uploaded study material or ask general questions without providing study material.

### 📄 Document Support

Supports:

- PDF
- DOCX
- TXT
- Manual text input

---

## 🌐 Live Application

The application is deployed and available online.

**Live Demo:** https://rahul-ai-study.streamlit.app

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- python-dotenv
- pypdf
- python-docx
- Git & GitHub

---

## 🏗️ Project Architecture

```text
User
 |
 v
Streamlit Interface
 |
 +----> Document Processing
 |          |
 |          +--> PDF
 |          +--> DOCX
 |          +--> TXT
 |
 v
Extracted Text
 |
 v
Prompt Generation
 |
 v
Gemini API
 |
 v
AI Response
 |
 v
Streamlit Interface

---

## 🔄 How It Works

1. The user uploads a PDF, DOCX or TXT file, or manually enters study material.
2. The application extracts the text from the uploaded document.
3. The user selects an AI feature such as Summarize, Explain, Generate Questions or Study Notes.
4. Python constructs an appropriate prompt based on the selected feature.
5. The prompt and study material are sent to the Gemini API.
6. Gemini generates the requested response.
7. The response is displayed through the Streamlit interface.
8. Users can also ask questions without uploading study material.

---

## 📁 Project Structure

```text
AI_STUDY_ASSISTANT/
│
├── app.py
├── ai_utils.py
├── document_utils.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── Screenshot/
    ├── main.png
    ├── summary.png
    ├── explain.png
    └── questions.png
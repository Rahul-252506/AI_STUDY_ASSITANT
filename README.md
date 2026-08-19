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
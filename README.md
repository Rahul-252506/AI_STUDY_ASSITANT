\# 🤖 AI Study \& Productivity Assistant



An AI-powered study assistant developed as part of the Innovation Hacks AI Internship.



The application uses Google's Gemini API to help students understand and revise study material through summarization, explanations, question generation, structured study notes and interactive Q\&A.



\---



\## 🚀 Features



\### 📝 Summarization

Converts lengthy study material into concise bullet-point summaries.



\### 💡 Explanation

Explains difficult concepts in simple language using examples and analogies where appropriate.



\### ❓ Question Generation

Generates 10 questions from the provided study material with varying difficulty levels from easy to hard, along with answers.



\### 📚 Study Notes

Converts study material into structured notes containing key concepts, definitions, examples and important exam points.



\### 🔍 Ask Questions

Allows users to ask questions about uploaded study material or ask general questions without providing study material.



\### 📄 Document Support

Supports:

\- PDF

\- DOCX

\- TXT

\- Manual text input



\---



\## 🛠️ Technologies Used



\- Python

\- Streamlit

\- Google Gemini API

\- python-dotenv

\- pypdf

\- python-docx

\- Git \& GitHub



\---



\## 🏗️ Project Architecture



```text

User

&#x20;|

&#x20;v

Streamlit Interface

&#x20;|

&#x20;+----> Document Processing

&#x20;|          |

&#x20;|          +--> PDF

&#x20;|          +--> DOCX

&#x20;|          +--> TXT

&#x20;|

&#x20;v

Extracted Text

&#x20;|

&#x20;v

Prompt Generation

&#x20;|

&#x20;v

Gemini API

&#x20;|

&#x20;v

AI Response

&#x20;|

&#x20;v

Streamlit Interface


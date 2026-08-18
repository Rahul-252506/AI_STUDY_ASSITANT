import os

import streamlit as st
from dotenv import load_dotenv
from google import genai

from ai_utils import generate_response
from document_utils import (
    extract_pdf_text,
    extract_docx_text,
    extract_txt_text
)


# ============================================================
# CONFIGURATION
# ============================================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Study & Productivity Assistant",
    page_icon="🤖",
    layout="wide"
)


# ============================================================
# CHECK API KEY
# ============================================================

if not api_key:

    st.error(
        "Gemini API key not found. "
        "Please add GEMINI_API_KEY to your .env file."
    )

    st.stop()


client = genai.Client(api_key=api_key)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("🤖 About")

    st.write(
        "AI Study & Productivity Assistant helps you "
        "understand, revise and practice your study material."
    )

    st.divider()

    st.subheader("Available Features")

    st.write("📝 Summarize")
    st.write("💡 Explain")
    st.write("❓ Generate Questions")
    st.write("📚 Study Notes")
    st.write("🔍 Ask Questions")

    st.divider()

    st.caption(
        "Innovation Hacks AI Internship — Week 1"
    )


# ============================================================
# MAIN HEADER
# ============================================================

st.title("🤖 AI Study & Productivity Assistant")

st.write(
    "Transform your study material into summaries, "
    "explanations, questions and structured notes."
)

st.info(
    "💡 Upload a PDF, DOCX or TXT file, or paste your "
    "study material below."
)


# ============================================================
# DOCUMENT UPLOAD
# ============================================================

st.subheader("📚 Study Material")

uploaded_file = st.file_uploader(
    "Upload your study material",
    type=["pdf", "docx", "txt"],
    help="Supported formats: PDF, DOCX and TXT"
)

text = ""


# ============================================================
# EXTRACT UPLOADED FILE
# ============================================================

if uploaded_file is not None:

    file_name = uploaded_file.name.lower()

    try:

        if file_name.endswith(".pdf"):

            text = extract_pdf_text(uploaded_file)

        elif file_name.endswith(".docx"):

            text = extract_docx_text(uploaded_file)

        elif file_name.endswith(".txt"):

            text = extract_txt_text(uploaded_file)

        if text.strip():

            st.success(
                f"✅ Loaded {uploaded_file.name}"
            ) 
            st.caption(f"Extracted approximately {len(text.split())} words.")

        else:

            st.warning(
                "The uploaded file does not contain "
                "extractable text."
            )

    except Exception as e:

        st.error(
            "Could not read the uploaded file."
        )

        st.caption(
            f"Error details: {e}"
        )


# ============================================================
# MANUAL TEXT INPUT
# ============================================================

manual_text = st.text_area(
    "Or paste your study material",
    height=200,
    placeholder="Paste your study material here..."
)


if uploaded_file is None and manual_text.strip():

    text = manual_text


# ============================================================
# QUESTION INPUT
# ============================================================

question = st.text_input(
    "❓ Ask a Question",
    placeholder="Example: What is the time complexity of binary search?"
)


# ============================================================
# BUTTONS
# ============================================================

st.subheader("Choose an Action")
col1, col2, col3, col4, col5 = st.columns(5)


with col1:

    summarize_button = st.button(
        "📝 Summarize",
        use_container_width=True
    )


with col2:

    explain_button = st.button(
        "💡 Explain",
        use_container_width=True
    )


with col3:

    questions_button = st.button(
        "❓ Generate Questions",
        use_container_width=True
    )


with col4:

    notes_button = st.button(
        "📚 Study Notes",
        use_container_width=True
    )


with col5:

    ask_button = st.button(
        "🔍 Ask Question",
        use_container_width=True
    )


# ============================================================
# SUMMARIZE
# ============================================================

if summarize_button:

    if not text.strip():

        st.warning(
            "Please upload a file or enter some text first."
        )

    else:

        prompt = f"""
        Summarize the following text in 5 concise bullet points.

        Keep the important information and make the language
        easy for a college student to understand.

        TEXT:
        {text}
        """

        try:

            with st.spinner("Generating summary..."):

                answer = generate_response(
                    client,
                    prompt
                )

            st.subheader("📝 Summary")

            st.write(answer)

        except Exception as e:

            st.error(
                "Something went wrong while generating the summary."
            )

            st.caption(
                f"Error details: {e}"
            )


# ============================================================
# EXPLAIN
# ============================================================

if explain_button:

    if not text.strip():

        st.warning(
            "Please upload a file or enter some text first."
        )

    else:

        prompt = f"""
        Explain the following content in simple,
        easy-to-understand language.

        Assume the user is a college student learning
        this topic for the first time.

        Do not simply shorten the content.

        Break difficult concepts into smaller parts.
        Use simple analogies or examples when helpful.
        Explain the why and how, not just the definition.

        CONTENT:
        {text}
        """

        try:

            with st.spinner("Preparing explanation..."):

                answer = generate_response(
                    client,
                    prompt
                )

            st.subheader("💡 Explanation")

            st.write(answer)

        except Exception as e:

            st.error(
                "Something went wrong while generating "
                "the explanation."
            )

            st.caption(
                f"Error details: {e}"
            )


# ============================================================
# GENERATE QUESTIONS
# ============================================================

if questions_button:

    if not text.strip():

        st.warning(
            "Please upload a file or enter some text first."
        )

    else:

        prompt = f"""
        Create 10 questions based ONLY on the content
        provided below.

        The questions should have varying difficulty:

        Questions 1-3: Easy
        Questions 4-7: Medium
        Questions 8-10: Hard

        Focus strictly on the information contained
        in the user's content.

        Do not introduce topics that are not supported
        by the provided content.

        Provide the correct answer immediately after
        each question.

        Make the questions useful for a college student's
        exam preparation.

        CONTENT:
        {text}
        """

        try:

            with st.spinner("Generating questions..."):

                answer = generate_response(
                    client,
                    prompt
                )

            st.subheader("❓ Practice Questions")

            st.write(answer)

        except Exception as e:

            st.error(
                "Something went wrong while generating questions."
            )

            st.caption(
                f"Error details: {e}"
            )


# ============================================================
# STUDY NOTES
# ============================================================

if notes_button:

    if not text.strip():

        st.warning(
            "Please upload a file or enter some text first."
        )

    else:

        prompt = f"""
        Create structured study notes from the content below.

        Organize the notes using clear headings and bullet points.

        Include, when supported by the content:

        1. Main topic
        2. Important concepts
        3. Key points
        4. Important definitions
        5. Examples
        6. Formulas or complexity information
        7. Important exam points

        Use simple language suitable for a college student.

        Do not introduce information that is not supported
        by the provided content.

        CONTENT:
        {text}
        """

        try:

            with st.spinner("Creating study notes..."):

                answer = generate_response(
                    client,
                    prompt
                )

            st.subheader("📚 Study Notes")

            st.write(answer)

        except Exception as e:

            st.error(
                "Something went wrong while creating study notes."
            )

            st.caption(
                f"Error details: {e}"
            )


# ============================================================
# ASK QUESTION
# ============================================================

if ask_button:

    if not question.strip():

        st.warning(
            "Please enter a question first."
        )

    else:

        # Study material available
        if text.strip():

            prompt = f"""
            You are an AI study assistant.

            Answer the user's question based primarily
            on the provided study material.

            If the answer is not available in the provided
            material, you may use your general knowledge,
            but clearly mention that the information was
            not found in the provided material.

            Give a clear explanation suitable for a
            college student.

            STUDY MATERIAL:
            {text}

            USER QUESTION:
            {question}
            """

        # No study material
        else:

            prompt = f"""
            You are an AI study assistant.

            Answer the following question clearly and
            accurately for a college student.

            Explain the concept in simple language.
            Use an example when helpful.

            USER QUESTION:
            {question}
            """

        try:

            with st.spinner("Thinking..."):

                answer = generate_response(
                    client,
                    prompt
                )

            st.subheader("🔍 Answer")

            st.write(answer)

        except Exception as e:

            st.error(
                "Something went wrong while getting the answer."
            )

            st.caption(
                f"Error details: {e}"
            )
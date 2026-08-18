from pypdf import PdfReader
from docx import Document


def extract_pdf_text(uploaded_file):

    reader = PdfReader(uploaded_file)

    extracted_text = []

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            extracted_text.append(page_text)

    return "\n\n".join(extracted_text)


def extract_docx_text(uploaded_file):

    document = Document(uploaded_file)

    paragraphs = []

    for paragraph in document.paragraphs:

        if paragraph.text.strip():
            paragraphs.append(paragraph.text)

    return "\n\n".join(paragraphs)


def extract_txt_text(uploaded_file):

    return uploaded_file.getvalue().decode("utf-8")
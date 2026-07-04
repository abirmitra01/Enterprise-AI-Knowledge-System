from docx import Document


def extract_docx_text(filepath):

    doc = Document(filepath)

    text = ""

    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"

    return text
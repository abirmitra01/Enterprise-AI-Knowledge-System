import os

from app.processors.pdf_processor import extract_pdf_text
from app.processors.docx_processor import extract_docx_text
from app.processors.ppt_processor import extract_ppt_text
from app.processors.txt_processor import extract_txt_text

from app.utils.text_cleaner import clean_text
from app.services.embedding_service import create_embeddings


PROCESSED_FOLDER = "processed"


def process_document(filepath):

    extension = filepath.split(".")[-1].lower()

    if extension == "pdf":
        text = extract_pdf_text(filepath)

    elif extension == "docx":
        text = extract_docx_text(filepath)

    elif extension == "pptx":
        text = extract_ppt_text(filepath)

    elif extension == "txt":
        text = extract_txt_text(filepath)

    else:
        raise Exception("Unsupported document.")

    # Clean the extracted text
    text = clean_text(text)
    create_embeddings(
    text,
    os.path.basename(filepath)
)
    # Create processed folder if it doesn't exist
    os.makedirs(PROCESSED_FOLDER, exist_ok=True)

    # Output file path
    filename = os.path.basename(filepath)

    output = os.path.join(
        PROCESSED_FOLDER,
        filename + ".txt"
    )

    with open(
        output,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(text)
    try:
        ...
    except Exception as e:
        raise Exception(
        f"Processing failed: {e}"
    )

    return output
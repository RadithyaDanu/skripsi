from pypdf import PdfReader


def load_pdf(path):
    reader = PdfReader(path)

    documents = []

    for page_number, page in enumerate(reader.pages):
        text = page.extract_text()

        if text:
            documents.append({
                "page": page_number + 1,
                "text": text
            })

    return documents

import fitz
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 600,
        chunk_overlap = 100,
        separators=["\n\n", "\n", " ", ""]
    )

content = fitz.open("sample_test_document.pdf")
chunks = []

for i, page in enumerate(content):
    data = page.get_text().strip()
    chunk = text_splitter.split_text(data)

    for c in chunk:
        chunks.append({
            "page_number":i+1,
            "text": c
        })

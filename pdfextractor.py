import fitz
from docx import Document
import os
import requests
from urllib.parse import urlparse

def download_pdf(url, local_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(local_path, 'wb') as f:
            f.write(response.content)
        return local_path
    else:
        print(f"Error: Unable to download the PDF from '{url}'. Status code: {response.status_code}")
        return None

# Input PDF file or URL
pdf_input = "https://www2.miamidadeclerk.gov/ocs/ImgViewerWF.aspx?QS=B6%2f9EwnZlIiih%2bgqiU8rawLJW%2bj4E30XGWoN6L%2b82TlrI6ZKeBzZWEcmY6diy%2bbNvNcDVi9gRoQMfgufYMwZCEVFoj5IoptRFNP%2fx1SkmMQh8tc3zUN%2beUf8qEcBKoFwQ%2bVubIyJ5TdTYOjDh2WdRe5GivwuoM%2b407AC4fDr9HaHFltRzczAmIJEipn2YAV9EnzaAM3Ga2UKIuvtAVP1astLJBTnDma6BcNVz4zP%2flcVP2f7qBpvOIoZQUGdgbl1VqTOAqy3I1pzYfjcq5SgH8Wi5EaIZwYsIGwDeSTTtDvzmkCZyVUIJA%3d%3d"

# Check if the input is a URL
parsed_url = urlparse(pdf_input)
if parsed_url.scheme in ('http', 'https'):
    pdf_document = download_pdf(pdf_input, "downloaded.pdf")
else:
    pdf_document = pdf_input

# Check if the file exists
if not pdf_document or not os.path.exists(pdf_document):
    print(f"Error: The file '{pdf_document}' does not exist.")
else:
    document = fitz.open(pdf_document)

    # Initialize an empty string to hold all the extracted text
    all_text = ""

    # Create a new Word document
    doc = Document()

    # Iterate through each page
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        all_text += page.get_text()

    # Add the extracted text to the Word document
    doc.add_paragraph(all_text)

    # Save the Word document
    doc.save("extracted_text.docx")
    print("Text extracted and saved to 'extracted_text.docx'")
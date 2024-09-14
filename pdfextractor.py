import fitz
from docx import Document
import subprocess
import os

def download_pdf_with_puppeteer():
    try:
        subprocess.run(["node", "download_pdf.js"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None

# Download the PDF using Puppeteer
download_pdf_with_puppeteer()

# Path to the downloaded PDF
download_dir = os.path.expanduser("~/Downloads")  # Adjust this path if needed
pdf_document = os.path.join(download_dir, "downloaded.pdf")  # Update this filename if needed

if not os.path.exists(pdf_document):
    print(f"Error: The file '{pdf_document}' could not be found.")
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
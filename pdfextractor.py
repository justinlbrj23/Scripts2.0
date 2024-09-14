import requests
from requests.exceptions import ConnectTimeout
import fitz  # Import the 'fitz' module

def download_pdf(url, filename):
    try:
        response = requests.get(url, timeout=10)  # Set a timeout of 10 seconds
        response.raise_for_status()  # Raise an exception for HTTP errors
        with open(filename, 'wb') as f:
            f.write(response.content)
        return filename
    except ConnectTimeout:
        print(f"Error: Connection to {url} timed out.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Example usage
pdf_input = "https://www2.miamidadeclerk.gov/ocs/ImgViewerWF.aspx?QS=B6%2F9EwnZlIiih%2BgqiU8rawLJW%2Bj4E30XGWoN6L%2B82TlrI6ZKeBzZWEcmY6diy%2BbNvNcDVi9gRoQMfgufYMwZCEVFoj5IoptRFNP%2Fx1SkmMQh8tc3zUN%2BeUf8qEcBKoFwQ%2BVubIyJ5TdTYOjDh2WdRe5GivwuoM%2B407AC4fDr9HaHFltRzczAmIJEipn2YAV9EnzaAM3Ga2UKIuvtAVP1astLJBTnDma6BcNVz4zP%2FlcVP2f7qBpvOIoZQUGdgbl1VqTOAqy3I1pzYfjcq5SgH8Wi5EaIZwYsIGwDeSTTtDvzmkCZyVUIJA%3D%3D"
pdf_document = download_pdf(pdf_input, "downloaded.pdf")

if pdf_document is None:
    print(f"Error: The file '{pdf_input}' could not be downloaded.")
else:
    document = fitz.open(pdf_document)

    # Initialize an empty string to hold all the extracted text
    all_text = ""

    from docx import Document
    
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
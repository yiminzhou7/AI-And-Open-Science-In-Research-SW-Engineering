import os
import requests
from bs4 import BeautifulSoup


def grobid_xml(pdf_path):
    """
    Extracts XML content from a PDF file using the Grobid API.
    INPUT:
    - pdf_path (str): Path to the PDF file to be processed.

    OUTPUT:
    - BeautifulSoup object representing the XML response from Grobid if successful,
      None otherwise.
    """
    
    grobid_url = 'http://localhost:8070/api/processFulltextDocument'
    with open(pdf_path, 'rb') as file:
        # Create the request to send to the Grobid API
        params = {'input': (pdf_path, file, 'application/pdf')}
        # Send the request to the Grobid API
        response = requests.post(grobid_url, files=params)
        if response.status_code == 200:
            # Parse the XML response from Grobid
            soup = BeautifulSoup(response.text, 'xml')
        else:
            print(f"Error: Failed to retrieve content from {pdf_path}. Status code: {response.status_code}") 
            return None
    return soup


### docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2

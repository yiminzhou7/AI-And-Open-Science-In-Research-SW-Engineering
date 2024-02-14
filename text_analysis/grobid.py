import os
import requests
from bs4 import BeautifulSoup

def grobid_response(pdf_path):
    """
    

    INPUT:
    - articles_folder(str): Path to the folder containing the PDF files.

    OUTPUT:
    - Content of the response of Grobid.
    """
    # URL of the Grobid API to extract the abstract
    grobid_url = 'http://localhost:8070/api/processFulltextDocument'
    with open(pdf_path, 'rb') as file:
        # Create the request to send to the Grobid API
        files = {'input': (pdf_path, file, 'application/pdf')}
        # Send the request to the Grobid API
        response = requests.post(grobid_url, files=files)
        if response.status_code == 200:
            # Parse the XML response from Grobid
            soup = BeautifulSoup(response.text, 'xml')
            return soup
        else:
            print(f"Error: Failed to retrieve content from {pdf_path}. Status code: {response.status_code}")
            return None
        



def grobid_responses(articles_folder):
    grobid_url = 'http://localhost:8070/api/processFulltextDocument'
    # Verify the path
    if not os.path.isdir(articles_folder):
        print('The specified path is not a valid folder.')
        return []

    # List to store the responses from Grobid
    all_responses = []

    for filename in os.listdir(articles_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(articles_folder, filename)
            with open(pdf_path, 'rb') as file:
                # Create the request to send to the Grobid API
                files = {'input': (pdf_path, file, 'application/pdf')}
                # Send the request to the Grobid API
                response = requests.post(grobid_url, files=files)
                if response.status_code == 200:
                    # Parse the XML response from Grobid
                    soup = BeautifulSoup(response.text, 'xml')
                    all_responses.append(soup)
                else:
                    print(f"Error: Failed to retrieve content from {pdf_path}. Status code: {response.status_code}") 
    return all_responses

### docker run --rm --init --ulimit core=0 -p 8070:8070 lfoppiano/grobid:0.8.0
### docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2

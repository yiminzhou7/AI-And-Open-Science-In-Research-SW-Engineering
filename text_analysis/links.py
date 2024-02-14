import re

def extract_links(grobid_results):
    """
    Extract links from PDF files in the specified folder using Grobid.

    INPUT:
    - grobid_results(List): List of results of Grobid..

    OUTPUT:
    - List of lists containing links found in each paper.
    """

    # Verify that grobid_results is not empty
    if not grobid_results:
         return []
    
    list_links = []
    for result in grobid_results:
        if result is not None:
            # Find all <ref> elements within the XML document
            text = result.get_text(strip=True)

            # Define a regular expression pattern to match URLs
            url_pattern = re.compile(r"(?:(?:https?://|www\.)\S+|\(https?://\S+\))")
            # Find all matches of the URL pattern in the text
            links = re.findall(url_pattern, text)
            list_links.append(links)
    
    return list_links
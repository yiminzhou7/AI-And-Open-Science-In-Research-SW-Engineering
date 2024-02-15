import re


def extract_links(xml):
    """
    Extracts links from an XML document obtained from Grobid processing.

    INPUT:
    - xml (BeautifulSoup): BeautifulSoup object representing the XML document.

    OUTPUT:
    - List of unique links found in the XML document.

    """

    # Verify that grobid_results is not empty
    if not xml:
        return []
    else:
        text = xml.get_text(strip=True)
        # Define a regular expression pattern to match URLs
        url_pattern = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
        # Find all matches of the URL pattern in the text
        links = re.findall(url_pattern, text)

        # Extract links from 'ptr' elements
        ptr_elements = xml.find_all('ptr')
        for ptr in ptr_elements:
            links.append(ptr["target"])
    
    return list(set(links))


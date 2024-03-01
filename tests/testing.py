import sys
import os

import unittest
from bs4 import BeautifulSoup

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

import text_analysis.figures as fig
import text_analysis.abstract as ab
import text_analysis.links as lk


def get_xml(xml_file):
    """
    Parse the XML file and return a BeautifulSoup object.

    IMPUT:
    - xml_file (str): path of the XML file.

    OUTPUT:
    - soup (BeautifulSoup): BeautifulSoup object representing the XML content.
    """
    with open(xml_file, 'r', encoding="utf-8") as file:
        xml_content = file.read()
        soup = BeautifulSoup(xml_content, 'xml')
    return soup


class text_analysis_test(unittest.TestCase):

    # Test that should return None since there is no abstract
    def test_no_abstract(self):
        xml = get_xml("tests/xml/no_abs.xml")
        self.assertIsNone(ab.extract_abstract(xml), "Test failed: abstract should be None")

    # Test that should return 0 sice there is no figure
    def test_figures1(self):
        xml = get_xml("tests/xml/no_abs.xml")
        self.assertEqual(fig.count_figures(xml), 0, "Test failed: count_figures should be 0")

    # Test that should return 1 figure
    def test_figures2(self):
        xml = get_xml("tests/xml/AI_healthcare-3.xml")
        self.assertEqual(fig.count_figures(xml), 1, "Test failed: count_figures should be 1")
    
    # Test that should return an empty list since there is not url
    def test_no_url(self):
        xml = get_xml("tests/xml/AI_healthcare-3.xml")
        self.assertEqual(lk.extract_links(xml), [], "Test failed: extract_links should return an empty list")
    
    # Test that should return the urls
    def test_url1(self):
        xml = get_xml("tests/xml/Artificial_Intelligence_and_Pain_Medicine.xml")
        expected_urls = ["https://www.dovepress.com/journal-of-pain-research-journal", "https://doi.org/10.2147/JPR.S429594"]
        self.assertCountEqual(lk.extract_links(xml), expected_urls, "Test failed: extract_links should return the expected URLs")



if __name__ == "__main__":
    unittest.main()

## desde directorio raíz
## python "tests/testing.py"
import unittest
from bs4 import BeautifulSoup

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
        try:
            assert ab.extract_abstract(xml) is None
            print("Test test_no_abstract OK!")
        except AssertionError:
            print("Test test_no_abstract failed!")

    # Test that should return 0 sice there is no figure
    def test_figures1(self):
        xml = get_xml("tests/xml/no_abs.xml")
        try:
            assert fig.count_figures(xml) == 0
            print("Test test_figures1 OK!")
        except AssertionError:
            print("Test test_figures1 failed!")

    # Test that should return 1 figure
    def test_figures2(self):
        xml = get_xml("tests/xml/AI_healthcare-3.xml")
        try:
            assert fig.count_figures(xml) == 1
            print("Test test_figures2 OK!")
        except AssertionError:
            print("Test test_figures2 failed!")
    
    # Test that should return an empty list since there is not url
    def test_no_url(self):
        xml = get_xml("tests/xml/AI_healthcare-3.xml")
        try:
            assert lk.extract_links(xml) == []
            print("Test test_no_url OK!")
        except AssertionError:
            print("Test test_no_url failed!")
    
    # Test that should return the urls
    def test_url1(self):
        xml = get_xml("tests/xml/Artificial_Intelligence_and_Pain_Medicine.xml")
        try:
            self.assertCountEqual(lk.extract_links(xml), ["https://www.dovepress.com/journal-of-pain-research-journal", "https://doi.org/10.2147/JPR.S429594"])
            print("Test test_url1 OK!")
        except AssertionError:
            print("Test test_url1 failed!")



## desde directorio raíz
## python -m unittest tests.testing
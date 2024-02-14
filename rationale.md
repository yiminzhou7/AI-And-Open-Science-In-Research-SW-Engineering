# Rationale for Text Analysis of 10 Open Access Papers in PDF Format
This document provides a rationale for the validation process used to ensure the accuracy and reliability of the answers provided in the repository documentation.

To complete the three sections, **Grobid** was used.
Upon receiving a PDF file, Grobid processes the document and returns the extracted information in XML format. 
This XML data is then parsed to extract the desired information, such as abstracts, figures, and links, for further analysis and visualization. 

## Validation of keyword cloud of abstract information
from the XML data obtained from Grobid. This extraction process involved identifying the **`<abstract>`** tags within the XML structure
Following extraction, the abstracts underwent preprocessing steps, including converting words to lowercase, removing punctuation, stopwords, and lemmatizing the words. 
Libraries such as `nltk` and `spacy` have been used.

After preprocessing, the abstracts were combined into a single text, from which the word cloud was generated using the `wordcloud` library in Python.
The generated image is saved in the folder **results** as "wordcloud.png".

To validate the results, a manual comparison with the original papers was performed to ensure the accuracy of the extracted abstracts and the generated word cloud.


## Validation of Visualization of numbers of figures per paper
The visualization of the number of figures per paper was achieved by counting the occurrences of **`<figure>`** tags in the XML representation of each PDF document. 
This count was then used to create a histogram illustrating the distribution of figures across the set of papers.

 The accuracy of the visualization depicting the number of figures per paper was confirmed by comparing the histogram data with the actual content of the papers.


## Validation of List of links 
The list of links extraction was performed using regular expressions to identify URLs within the extracted text. 

To validate the accuracy of the extracted links, each link was manually verified by accessing the original papers and comparing them with the extracted URLs.

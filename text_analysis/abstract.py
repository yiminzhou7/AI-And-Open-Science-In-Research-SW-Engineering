from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy


def extract_abstract(xml):
    """
    Extracts the abstract from an XML document obtained from Grobid processing.

    INPUT:
    - xml (BeautifulSoup): BeautifulSoup object representing the XML document.

    OUTPUT:
    - Abstract text extracted from the XML document.
    """

    # Verify that grobid_results is not empty
    if not xml:
        return None
    else:
        abstract = xml.find('abstract')
        if abstract:
            return abstract.text.strip()
        else:
            return None


def process_abstract(abstract):
    """
    Processes the given abstract text by converting it to lowercase, removing punctuation,
    stopwords, and performing lemmatization.

    INPUT:
    - abstract (str): The abstract text to be processed.

    OUTPUT:
    - Processed abstract text after applying the specified transformations.
    """
    
    if not abstract:
        return None
    else:
        abstract = abstract.lower()  # convert to lowercase
        abstract = re.sub(r'[^a-zA-Z\s]', '', abstract) # remove punctuation
        tokens = word_tokenize(abstract)  # tokenize the abstract
        # # remove stopwords
        stop_words = set(stopwords.words('english')) 
        filtered_abstract = [word for word in tokens if word not in stop_words]

        # lemmatization
        nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
        doc = nlp(' '.join(filtered_abstract))
        final_abstract = ' '.join([token.lemma_ for token in doc])
    
    return final_abstract


def generate_word_cloud(text, output_path):
    """
    Generate a word cloud from the provided text and save it as a PNG file.

    INPUT:
    - text (str): the text to generate the word cloud from.
    - output_path (str): the path where the word cloud PNG file will be saved.
    """
    # Create word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    # Display the word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')

    # Save the word cloud as a PNG file
    wordcloud.to_file(output_path)

    print(f"Word cloud saved as {output_path}")


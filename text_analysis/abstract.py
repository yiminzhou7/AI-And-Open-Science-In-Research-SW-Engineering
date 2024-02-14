from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy
# Descargar el modelo de lenguaje en inglés para spaCy
import spacy.cli
# spacy.cli.download("en_core_web_sm")  # descomentar si no lo tenemos descargado



def extract_abstracts(grobid_results):
    """
    Extract abstract from PDF files in the specified folder using Grobid.

    INPUT:
    - grobid_results(List): List of results of Grobid.

    OUTPUT:
    - List of abstracts extracted from the PDF files.
    """

    # Verify that grobid_results is not empty
    if not grobid_results:
         return []

    # List to store the extracted abstracts
    abstracts = []

    for result in grobid_results:
        if result is not None:
            abstract = result.find('abstract').text.strip()
            abstracts.append(abstract)
    return abstracts



def process_abstracts(abstracts):
    """
    Clean and process the abstracts.

    INPUT: 
    - abstracts (list of str): List of abstracts.

    OUTPUT:
    - List of processed abstracts.
    """

    final_abstracts = []
    for abstract in abstracts:
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
        final_abstracts.append(final_abstract)
    
    return final_abstracts


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

    # Show the saved file path
    plt.show()

    print(f"Word cloud saved as {output_path}")


# articles_folder = input('Enter articles folder: ')
# grobid_results = grobid_responses(articles_folder)
# raw_abstracts = extract_abstracts(grobid_results)

# final_abstracts = process_abstracts(raw_abstracts)

# # Convert all processed abstracts into a single text
# combined_text = ' '.join(final_abstracts)
# print(combined_text)


# generate_word_cloud(combined_text, './results/wordcloud.png')

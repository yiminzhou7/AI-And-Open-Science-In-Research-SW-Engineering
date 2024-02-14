from text_analysis.grobid import grobid_responses
from text_analysis.abstract import extract_abstracts, process_abstracts, generate_word_cloud
from text_analysis.figures import count_figures, histogram
from text_analysis.links import extract_links

def main():
    # Input folder containing PDF files
    articles_folder = input('Enter articles folder: ')
    # extract results in xml with Grobid
    grobid_results = grobid_responses(articles_folder)
    

    # WORDCLOUD
    # Extract abstracts from PDF files
    raw_abstracts = extract_abstracts(grobid_results)

    # Process the abstracts
    final_abstracts = process_abstracts(raw_abstracts)

    # Convert all processed abstracts into a single text
    combined_text = ' '.join(final_abstracts)

    # Generate and save the word cloud
    generate_word_cloud(combined_text, './results/wordcloud.png')
    print('--------------------------------------------------------')

    # -------------------------------------------------------------
    # FIGURES
    # count figures per article
    figures = count_figures(grobid_results)
    # generate the histogram and save it
    histogram(figures, './results/figures.png')
    print('--------------------------------------------------------')

    #---------------------------------------------------------------
    # LINKS
    list_links = extract_links(grobid_results)
    for i, links in enumerate(list_links):
        print(f'Paper {i}:')
        print(links)
        print('-------------------')

if __name__ == "__main__":
    main()
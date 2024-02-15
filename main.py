import os
import text_analysis.grobid as gb
import text_analysis.abstract as ab
import text_analysis.figures as fig
import text_analysis.links as lk

def main():
    # Input folder containing PDF files
    articles_folder = input('Enter articles folder: ')

    list_abstracts = []
    count_figures = []

    for filename in os.listdir(articles_folder):
        if filename.endswith(".pdf"):
            # EXTRACT XML USING GROBID 
            pdf_path = os.path.join(articles_folder, filename)
            print(f'Extracting XML from {filename}...')
            xml = gb.grobid_xml(pdf_path)

            # WORDCLOUD
            print(f'Processing abstract from {filename}...')
            raw_abstract = ab.extract_abstract(xml)
            final_abstract = ab.process_abstract(raw_abstract)
            list_abstracts.append(final_abstract)
            
            # NUMBER OF FIGURES PER PAPER
            print(f'Counting figures from {filename}...')
            figures = fig.count_figures(xml)
            count_figures.append(figures)

            # LINKS
            print(f'Extracting links from {filename}...')
            links = lk.extract_links(xml)
            print(f'URLs from {filename}:')
            for link in links:
                print(link)
        
        print()

    # Convert all processed abstracts into a single text
    combined_text = ' '.join(list_abstracts)

    # Generate and save the word cloud
    print("Generating wordcloud of abstracts...")
    ab.generate_word_cloud(combined_text, './results/wordcloud.png')
    
    # generate the histogram and save it
    print("Generating histogram of figures...")
    fig.histogram(count_figures, './results/figures.png')
    











if __name__ == "__main__":
    main()
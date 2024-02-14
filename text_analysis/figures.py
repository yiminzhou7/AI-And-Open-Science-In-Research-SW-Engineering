import matplotlib.pyplot as plt


def count_figures(grobid_results):
    """
    Count the number of figures from PDF files in the specified folder using Grobid.

    INPUT:
    - grobid_results(List): List of results of Grobid..

    OUTPUT:
    - List of number of figures per article.
    """

    # Verify that grobid_results is not empty
    if not grobid_results:
         return []
    
    fig_count = []
    for result in grobid_results:
        if result is not None:
            # Find all <figure> elements within the XML document
            figures = result.find_all('figure')
            # Count the number of figures
            fig_count.append(len(figures))            
    return fig_count


def histogram(fig_count, output_path):
    """
    Draw a histogram of the number of figures per article and save it as a PNG file.

    INPUT:
    - fig_count (list): List of number of figures per article.
    - output_path (str): Path where the histogram PNG file will be saved.
    """
    article_indices = list(range(1, len(fig_count) + 1))  # Indices representing the articles
    plt.figure(figsize=(10, 6))
    plt.bar(article_indices, fig_count, color='blue')
    plt.xlabel('Article')
    plt.ylabel('Number of Figures')
    plt.title('Histogram of Number of Figures per Article')
    plt.grid(True)
    plt.savefig(output_path)
    plt.show()
    print(f"Histogram saved as {output_path}")
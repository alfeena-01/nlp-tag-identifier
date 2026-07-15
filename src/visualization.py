import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk

def plot_frequency(tokens, n=30):
    """
    Plot frequency distribution of tokens.
    """
    freq = nltk.FreqDist(tokens)
    freq.plot(n, cumulative=False)

def generate_wordcloud(tokens, output_path=None):
    """
    Generate and optionally save a word cloud.
    """
    wordcloud = WordCloud(width=800, height=400).generate(" ".join(tokens))
    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    
    if output_path:
        wordcloud.to_file(output_path)

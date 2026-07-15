📝 Tag Identifier Project

📌 Overview

This project performs text mining and named entity recognition (NER) on Wikipedia articles. It scrapes content, cleans and tokenizes text, visualizes word frequencies and word clouds, and extracts named entities such as organizations, people, and locations.

⚙️ Features

•Web Scraping: Collects text from Wikipedia using BeautifulSoup.

•Preprocessing: Tokenizes, removes stopwords/punctuation, and lemmatizes words with NLTK.

•Visualization: Generates frequency distribution plots and word clouds.

•Named Entity Recognition (NER): Identifies entities like ORGANIZATION, PERSON, and LOCATION.

•Data Export: Saves top words (top_words.csv) and extracted entities (entities.csv) into the data/ folder.

📂 Project Structure

nlp-tag-project/
│
├── src/
│   ├── scraper.py          # Scrapes Wikipedia text
│   ├── preprocessing.py    # Cleans and tokenizes text
│   └── visualization.py    # Frequency plots & word clouds
│
├── notebooks/
│   └── tag_identifier.ipynb  # Main notebook workflow
│
├── data/
│   ├── top_words.csv       # Top 50 frequent words
│   └── entities.csv        # Named entities with labels
│
└── README.md

🚀 How to Run

1. Install dependencies:
 pip install beautifulsoup4 html5lib nltk matplotlib wordcloud pandas

2. Open notebooks/tag_identifier.ipynb in Jupyter.

3. Run cells in order:

•Scrape Wikipedia text

•Preprocess tokens

•Visualize frequency & word cloud

•Perform NER

•Save results to CSV

✅ Outputs

•Graph: Word frequency distribution.

•Image: Word cloud visualization.

•CSV files:

  top_words.csv → most frequent words.

  entities.csv → extracted named entities.

### Known Limitations

- NLTK's default Named Entity Recognition (NER) may not detect entities in long, complex Wikipedia articles.
- The pipeline runs successfully, but `entities.csv` may be empty depending on the text.
- Future improvement: integrate spaCy for more accurate NER results.
    

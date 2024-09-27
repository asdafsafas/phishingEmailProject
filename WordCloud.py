# nltk.download('stopwords')

import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords

# stopwords is to exclude out words like "is, to , the, like..."
# nltk.download('stopwords')
# stop_words = set(stopwords.words('english'))

# Read the CSV file
try:
    df = pd.read_csv('spam_emails_dataset.csv') 
    print("CSV file loaded successfully.")
except FileNotFoundError:
    print("CSV file not found. Please check the file path.")
    df = pd.DataFrame() 

# Check if the DataFrame is not empty
if not df.empty:
    # Combine all text data into a single string
    word_string = ' '.join(df['text'].astype(str))

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

wordcloud = WordCloud(stopwords=STOPWORDS, background_color='black', max_words = 15).generate(word_string)

plt.figure(figsize=(7,3))
plt.clf()
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
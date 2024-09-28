import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Download the NLTK stopwords if not already downloaded
nltk.download('stopwords')

# Get the default English stopwords from NLTK
nltk_stopwords = set(stopwords.words('english'))

# Define your custom stopwords
custom_stopwords = {'http', 'subject', 'com', 'enron', 'www', 'ect'}

# Combine NLTK stopwords with custom stopwords
combined_stopwords = nltk_stopwords.union(custom_stopwords)

# Read the dataset
df = pd.read_csv('spam_emails_dataset.csv')

# Join all text into a single string and split into words
spam_words = " ".join(df[df['spam'] == 0]['text']).split()
ham_words = " ".join(df[df['spam'] == 1]['text']).split()

# Filter out stopwords from the word lists
filtered_spam_words = [word for word in spam_words if word.lower() not in combined_stopwords]
filtered_ham_words = [word for word in ham_words if word.lower() not in combined_stopwords]

# Generate the word clouds
spam_wordcloud = WordCloud(stopwords=combined_stopwords, background_color='black', max_words=15).generate(" ".join(filtered_spam_words))
ham_wordcloud = WordCloud(stopwords=combined_stopwords, background_color='black', max_words=15).generate(" ".join(filtered_ham_words))

# Plot the word clouds
plt.figure(figsize=(14,6))

plt.subplot(1, 2, 1)
plt.imshow(ham_wordcloud)
plt.title('Commonly used terms in Legitimate Emails')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(spam_wordcloud)
plt.title('Commonly used terms in Phishing Emails')
plt.axis('off')

plt.show()

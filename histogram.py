from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords

# Download the NLTK stopwords if not already downloaded
nltk.download('stopwords')

# Get the default English stopwords from NLTK
nltk_stopwords = set(stopwords.words('english'))

# Define your custom stopwords
custom_stopwords = {'http', 'subject', 'com', 'enron', 'www'}

# Add your custom stopwords to the existing stopwords set
stop_words = nltk_stopwords.union(custom_stopwords)

# Read the dataset
df = pd.read_csv('spam_emails_dataset.csv')

# Join all text into a single string and split into words
spam_words = " ".join(df[df['spam'] == 0]['text']).split()
ham_words = " ".join(df[df['spam'] == 1]['text']).split()

# Count. Standardize into lowercase, ensure no number, filter out stopwords
spam_word_freq = Counter([word.lower() for word in spam_words if word.lower() not in stop_words and word.isalpha()])
ham_word_freq = Counter([word.lower() for word in ham_words if word.lower() not in stop_words and word.isalpha()])

# Plot the bar charts
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.bar(*zip(*ham_word_freq.most_common(10)), color='y')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 10 Most Common Words in Legitimate Emails')
plt.xticks(rotation=45)

plt.subplot(1, 2, 2)
plt.bar(*zip(*spam_word_freq.most_common(10)), color='r')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 10 Most Common Words in Phishing Emails')
plt.xticks(rotation=45)

plt.show()

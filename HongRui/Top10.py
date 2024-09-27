from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import nltk
from nltk.corpus import stopwords

# stopwords is to exclude out words like "is, to , the, like..."
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Creating a DataFrame
df = pd.read_csv("spam_emails_dataset.csv")

# joining all into same string, add space in between, split again into list of words
spam_words = " ".join(df[df['spam'] == 0]['text']).split()
ham_words = " ".join(df[df['spam'] == 1]['text']).split()

# Count. Standalize into lowercase, ensure no number, filter out stopwords
spam_word_freq = Counter([word.lower() for word in ham_words if word.lower() not in stop_words and word.isalpha()])

plt.figure(figsize=(5, 3))
plt.bar(*zip(*spam_word_freq.most_common(10)), color='y')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 10 Most Common Words in Ham Emails')
plt.xticks(rotation=45)
plt.show()
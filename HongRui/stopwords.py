# Defining custom stopwords

# Import necessary libraries
import nltk
from nltk.corpus import stopwords

# Download the NLTK stopwords if not already downloaded
nltk.download('stopwords')

# Get the default English stopwords from NLTK
nltk_stopwords = set(stopwords.words('english'))

# Define your custom stopwords
custom_stopwords = {'http', 'subject', 'com', 'enron', 'www', 'ect'}

# Add your custom stopwords to the existing stopwords set
stop_words = nltk_stopwords.union(custom_stopwords)

# Now combined_stopwords contains both NLTK and custom stopwords
print(stop_words)

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.pipeline import Pipeline

# Load dataset from CSV file
data = pd.read_csv('spam_emails_dataset.csv', low_memory=False)  # Ensure the CSV has 'text' and 'spam' columns

# Check the number of samples
print(f"Number of samples: {len(data)}")
print(data.shape)

# Handle missing values: Option 1 - Remove rows with NaN values
data = data.dropna(subset=['text', 'spam'])

# Convert the 'text' column to strings (to handle any non-string values like integers)
data['text'] = data['text'].astype(str)

# Check the number of samples again after preprocessing
print(f"Number of samples after preprocessing: {len(data)}")
print(data.shape)

# Split the dataset into features and labels
X = data['text']  # Assuming the email text is in the 'text' column
y = data['spam']  # Assuming labels (0 for legitimate, 1 for phishing) are in the 'spam' column

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the models to compare
models = {
    "Logistic Regression": LogisticRegression(),
    "Random Forest": RandomForestClassifier(),
    "Naive Bayes": MultinomialNB(),
    "Support Vector Machine": SVC(probability=True)
}

# Initialize TfidfVectorizer for text data
vectorizer = TfidfVectorizer(stop_words='english')

# Dictionary to store results
results = {}

# Train and evaluate each model
for name, model in models.items():
    pipeline = Pipeline([('tfidf', vectorizer), ('model', model)])
    pipeline.fit(X_train, y_train)

    # Cross-validation for F1-score and ROC-AUC
    cv_f1 = cross_val_score(pipeline, X_train, y_train, cv=5, scoring='f1').mean()
    cv_roc_auc = cross_val_score(pipeline, X_train, y_train, cv=5, scoring='roc_auc').mean()

    # Evaluate on the test set
    y_pred = pipeline.predict(X_test)
    y_prob = pipeline.predict_proba(X_test)[:, 1]

    print(f"\n{name} Classification Report:")
    print(classification_report(y_test, y_pred))

    roc_auc = roc_auc_score(y_test, y_prob)
    print(f"ROC-AUC Score: {roc_auc:.4f}")

    # Store the results
    results[name] = {
        "F1-Score": cv_f1,
        "ROC-AUC": cv_roc_auc,
        "Test ROC-AUC": roc_auc
    }

# Compare the models
print("\nModel Selection Results:")
for name, metrics in results.items():
    print(f"{name}: F1-Score (CV) = {metrics['F1-Score']:.4f}, ROC-AUC (CV) = {metrics['ROC-AUC']:.4f}, Test ROC-AUC = {metrics['Test ROC-AUC']:.4f}")

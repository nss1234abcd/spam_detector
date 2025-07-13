import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import pickle

# Load dataset
df = pd.read_csv("dataset/spam.csv", encoding='latin-1')[['v1', 'v2']]
df.columns = ['label', 'message']

# Label encoding: ham = 0, spam = 1
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Vectorize text using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['message'])
y = df['label']

# Split and train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model and vectorizer
with open('saved_model/model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('saved_model/vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)
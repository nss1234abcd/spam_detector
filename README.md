# spam_detector
# Spam Messages Filtering

A machine learning-based web app to detect **spam messages**, classify their type (e.g., phishing, promotional, fraud), and identify the reason behind the prediction using keywords and indicators. Built with **Python, Streamlit**, and **Scikit-learn**.

##  Features
- Detects whether a message is **Spam** or **Safe**
- Categorizes spam as:
  - Phishing
  - Promotional
  - Fraud
- Highlights matched **keywords** and gives an **explanation**
- Extracts and displays **suspicious URLs**

----

## Tech Stack
- **Frontend**: Streamlit
- **Backend**: Python
- **ML Model**: Naive Bayes (Scikit-learn)
- **Vectorization**: TF-IDF
- **Dataset**: SMS Spam Collection (UCI)

----

**2. Install Dependencies**
It’s recommended to use a virtual environment.
pip install -r requirements.txt

**3. Train the Model (optional, already trained)**
python spam_classifier.py
This will generate:
saved_model/model.pkl
saved_model/vectorizer.pkl

**4. Run the Web App**
streamlit run app.py

Dataset Info
Name: SMS Spam Collection
Source: UCI Machine Learning Repository
Labels: spam, ham

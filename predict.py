import pickle
import re

# Load model and vectorizer
with open('saved_model/model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('saved_model/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Keyword categories
SPAM_CATEGORIES = {
    "Phishing": ["verify", "click", "account", "bank", "password", "login"],
    "Promotional": ["free", "offer", "win", "winner", "congratulations", "buy now"],
    "Fraud": ["lottery", "urgent", "limited", "claim", "transfer"],
}

# 🔍 Your explanation function
def explain_prediction(message):
    keywords = {
        'Phishing': ["click", "verify", "account", "login", "password"],
        'Advertisement': ["free", "win", "prize", "gift", "winner"],
        'Scam': ["urgent", "transfer", "amount", "otp"]
    }
    reason = []
    for category, words in keywords.items():
        for word in words:
            if word in message.lower():
                reason.append(word)
    return list(set(reason)) or ["No strong indicators"]

# 🔗 Extract URLs
def extract_urls(message):
    return re.findall(r'http[s]?://\S+', message)

# 📊 Prediction logic
def predict_message(message):
    vec_msg = vectorizer.transform([message])
    is_spam = model.predict(vec_msg)[0]

    result = {
        "label": "Spam" if is_spam else "Safe",
        "category": "N/A",
        "keywords": [],
        "urls": []
    }

    if is_spam:
        lowered = message.lower()
        for category, keywords in SPAM_CATEGORIES.items():
            matched_keywords = [kw for kw in keywords if kw in lowered]
            if matched_keywords:
                result["category"] = category
                result["keywords"] = matched_keywords
                break

        result["urls"] = extract_urls(message)

        # 👇 Add explanation keywords
        result["explanation"] = explain_prediction(message)

    return result
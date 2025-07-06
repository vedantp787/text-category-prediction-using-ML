"""
Task 2 – Text Category Prediction API

This Flask API loads the saved machine learning model and TF-IDF vectorizer.
It exposes a single POST endpoint '/predict' which accepts a sentence in JSON format,
and returns the predicted category as JSON.

Tested locally using PowerShell 
"""


from flask import Flask, request, jsonify
import joblib
import re

# Create Flask app
app = Flask(__name__)

model = joblib.load('text_category_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Function to clean text
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    return text

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()                
    sentence = data.get('sentence', '')      
    cleaned = clean_text(sentence)           
    vec = vectorizer.transform([cleaned])    
    pred = model.predict(vec)[0]             
    return jsonify({'category': pred})       

if __name__ == '__main__':
    app.run(debug=True)

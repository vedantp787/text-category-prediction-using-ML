
– Text Category Prediction

This project uses a machine learning model to predict the category of a given text 
(e.g., Ecommerce, Healthcare, Entertainment, Technology, Education, Other).  
The dataset was manually labeled, and the best performing model was deployed through a Flask API 
to provide real-time category predictions.


---

##  Files included

| File | Description |
|--|--|
| `Train.ipynb` | Notebook with preprocessing, data labeling process, model training and evaluation |
| `Prediction_File.ipynb` | Notebook that loads the saved model, asks user input and shows predicted category |
| `app.py` | Flask API file that serves predictions via a `/predict` POST endpoint |
| `text_category_model.pkl` | Saved machine learning model |
| `tfidf_vectorizer.pkl` | Saved TF-IDF vectorizer |

---

##  Process summary

- Manually labeled ~500 text samples into 6 categories: Ecommerce, Healthcare, Entertainment, Technology, Education, Other
- Explored multiple models and selected the best based on evaluation metrics
- Achieved ~70–75% accuracy by balancing data and fine-tuning preprocessing
- Built a Flask API to serve predictions




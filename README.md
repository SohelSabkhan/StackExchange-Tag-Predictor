# 🏷️ StackExchange Tag Predictor

This is a Streamlit web app that predicts relevant tags for questions based on StackExchange data using a fine-tuned DistilBERT model.

## 🚀 Features
- Enter a question and get intelligent tag suggestions.
- Adjustable confidence threshold for more/less specific results.
- Clean and responsive UI with a gradient background.
- Mobile-friendly and easy to use.

## 🧠 Model
- Fine-tuned DistilBERT for multi-label text classification.
- Trained on StackExchange question-tag pairs.
- Threshold-based prediction using sigmoid outputs.

## 📦 Files Included
- `app.py`: Streamlit app script.
- `multi-label-binarizer.pkl`: Label encoder.
- `distilbert-finetuned-imdb-multi-label/`: Saved model directory.

## 📲 Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py

from flask import Flask, render_template, request
import torch
import pickle
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import numpy as np

app = Flask(__name__)

# Load model, tokenizer and label binarizer
model = AutoModelForSequenceClassification.from_pretrained("distilbert-finetuned-stackexchange-multi-label")
tokenizer = AutoTokenizer.from_pretrained("distilbert-finetuned-stackexchange-multi-label")

with open("multi-label-binarizer.pkl", "rb") as f:
    multilabel = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    predicted_tags = []
    question = ""

    if request.method == "POST":
        question = request.form.get("question")

        if question.strip():
            encoding = tokenizer(question, return_tensors="pt", truncation=True, padding=True)
            encoding = {k: v.to(model.device) for k, v in encoding.items()}
            with torch.no_grad():
                outputs = model(**encoding)

            probs = torch.sigmoid(outputs.logits[0].cpu())
            preds = (probs >= 0.3).int().numpy()  # Default threshold fixed at 0.3
            predicted_tags = multilabel.inverse_transform(preds.reshape(1, -1))[0]

    return render_template("index.html", tags=predicted_tags, question=question)


if __name__ == "__main__":
    app.run(debug=True)

# 🏷️ StackExchange Tag Predictor

An AI-powered web application that automatically predicts relevant tags for StackExchange questions using a fine-tuned DistilBERT model. Simply enter your question and get instant tag suggestions to help categorize your content effectively.

## ✨ Features

- **AI-Powered Predictions**: Uses a fine-tuned DistilBERT model for accurate multi-label classification
- **Real-time Processing**: Get instant tag suggestions as you submit your question
- **Modern UI**: Beautiful, responsive interface with gradient designs and smooth animations
- **Multi-label Support**: Predicts multiple relevant tags for each question
- **Customizable Threshold**: Adjustable confidence threshold (default: 0.3) for tag predictions

## 🚀 Demo

Enter any programming or technical question, and the model will suggest relevant tags based on the content. Perfect for:
- Categorizing StackExchange questions
- Understanding question topics
- Learning about tag relevance in technical content

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone <your-repository-url>
cd stackexchange-tag-predictor
```

2. **Create and activate a virtual environment**
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install required packages**
```bash
pip install flask torch transformers numpy scikit-learn
```

4. **Download the model and required files**

Ensure you have the following files in your project directory:
- `distilbert-finetuned-stackexchange-multi-label/` (model directory)
- `multi-label-binarizer.pkl` (label encoder)

## 📁 Project Structure

```
stackexchange-tag-predictor/
│
├── app.py                                    # Flask application
├── multi-label-binarizer.pkl                 # Label encoder
│
├── distilbert-finetuned-stackexchange-multi-label/
│   ├── config.json
│   ├── pytorch_model.bin
│   └── ...
│
├── templates/
│   └── index.html                            # Main HTML template
│
├── static/
│   └── style.css                             # CSS styles (optional if embedded)
│
└── README.md                                 # This file
```

## 🎯 Usage

1. **Start the Flask application**
```bash
python app.py
```

2. **Open your browser**

Navigate to `http://127.0.0.1:5000/`

3. **Enter your question**

Type or paste your programming question in the textarea and click "Predict Tags"

4. **View predictions**

The model will display predicted tags based on your question content

## 🔧 Configuration

### Adjusting the Confidence Threshold

In `app.py`, you can modify the prediction threshold (default is 0.3):

```python
preds = (probs >= 0.3).int().numpy()  # Change 0.3 to your desired threshold
```

- **Lower threshold (0.2)**: More tags, but potentially less relevant
- **Higher threshold (0.5)**: Fewer tags, but more confident predictions

### Model Configuration

The application uses:
- **Model**: DistilBERT fine-tuned for multi-label classification
- **Tokenizer**: AutoTokenizer from the Transformers library
- **Framework**: PyTorch for inference

## 🧠 How It Works

1. **Input Processing**: User enters a question through the web interface
2. **Tokenization**: The question is tokenized using the DistilBERT tokenizer
3. **Model Inference**: The fine-tuned model processes the tokenized input
4. **Probability Calculation**: Sigmoid activation converts logits to probabilities
5. **Threshold Filtering**: Tags with probability ≥ 0.3 are selected
6. **Label Decoding**: Binary predictions are converted back to tag names
7. **Display**: Tags are shown in the UI with animations

## 📊 Model Details

- **Architecture**: DistilBERT (distilled version of BERT)
- **Task**: Multi-label text classification
- **Training Data**: StackExchange questions and tags
- **Output**: Multiple relevant tags per question

## 🎨 UI Features

- Gradient purple background with overlay effects
- Glassmorphic card design
- Smooth animations and transitions
- Responsive layout for mobile and desktop
- Tag animations with staggered appearance
- Hover effects for enhanced interactivity

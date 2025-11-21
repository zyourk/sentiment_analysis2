import os
from dotenv import load_dotenv
import torch
from huggingface_hub import login
from transformers import AutoModelForSequenceClassification, AutoTokenizer, logging
logging.set_verbosity(logging.CRITICAL)

load_dotenv()
token = os.getenv("HUGGINGFACE_HUB_TOKEN")
login(token)

# Device setup
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# Load model & tokenizer
model = AutoModelForSequenceClassification.from_pretrained("greyza/goemotions-longformer")
model.to(device)
model.eval()
tokenizer = AutoTokenizer.from_pretrained("greyza/goemotions-longformer")


def analyze(texts):
    """texts can be a single string or list of strings"""
    if isinstance(texts, str):
        texts = [texts]

    # Tokenize batch
    encodings = tokenizer(
        texts,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=2048
    ).to(device)

    with torch.no_grad():
        outputs = model(**encodings)
        scores = torch.softmax(outputs.logits, dim=-1)

    results = []
    for i, text in enumerate(texts):
        text_scores = scores[i]
        top_indices = text_scores.argsort(descending=True)
        pred_list = []
        for idx in top_indices:
            label = model.config.id2label[idx.item()]
            score = text_scores[idx].item()
            if label.lower() != "neutral":
                pred_list.append({"label": label, "score": score})
        results.append(pred_list[:5])

    # Return single result if input was single text
    return results if len(results) > 1 else results[0]

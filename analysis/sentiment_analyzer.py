import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("HF_TOKEN")

from huggingface_hub import login
login(token)

from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

model = AutoModelForSequenceClassification.from_pretrained("greyza/goemotions-longformer")
tokenizer = AutoTokenizer.from_pretrained("greyza/goemotions-longformer")

pipe = pipeline(
    "text-classification",
    model=model,
    tokenizer=tokenizer,
    top_k=None,
    truncation=True,
    device_map="auto"
)


def analyze(text):
    # Allow single text or list of texts
    if isinstance(text, list):
        predictions_batch = pipe(text, top_k=None, truncation=True)
        results = []
        for predictions in predictions_batch:
            preds = [p for p in predictions if p["label"].lower() != "neutral"]
            sorted_preds = sorted(preds, key=lambda x: x["score"], reverse=True)
            results.append(sorted_preds[:5])
        return results
    else:
        predictions = pipe(text, top_k=None, truncation=True)
        preds = [p for p in predictions if p["label"].lower() != "neutral"]
        sorted_preds = sorted(preds, key=lambda x: x["score"], reverse=True)
        return sorted_preds[:5]

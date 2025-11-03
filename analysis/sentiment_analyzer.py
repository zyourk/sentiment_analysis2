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
    truncation=True
)


def analyze(text):
    predictions = pipe(text, top_k=None)

    # Handle if predictions is a list of dicts
    if isinstance(predictions, list):
        if isinstance(predictions[0], dict):
            preds = predictions
        elif isinstance(predictions[0], list):  # Sometimes it's wrapped in another list
            preds = predictions[0]
        else:
            raise TypeError(f"Unexpected prediction format: {type(predictions[0])}")
    elif isinstance(predictions, dict):
        preds = [predictions]
    else:
        raise TypeError(f"Unexpected predictions type: {type(predictions)}")

    preds = [p for p in preds if p["label"].lower() != "neutral"]

    # Now preds should be a list of {label, score} dicts
    sorted_preds = sorted(preds, key=lambda x: x["score"], reverse=True)

    return sorted_preds[:5]
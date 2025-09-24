# attempting to get rid of warnings just to make output terminal prettier,
# but alas it does not work
import warnings
warnings.simplefilter("ignore", category=DeprecationWarning)
warnings.simplefilter("ignore", category=FutureWarning)
warnings.simplefilter("ignore", category=ResourceWarning)


from transformers import pipeline
pipe = pipeline(task='text-classification', model='SamLowe/roberta-base-go_emotions')


def analyze(text):
    inputs = pipe.tokenizer(text, return_overflowing_tokens=True, max_length=512, truncation=True)
    results = []
    for input_ids in inputs["input_ids"]:
        chunk_text = pipe.tokenizer.decode(input_ids, skip_special_tokens=True)
        results.extend(pipe(chunk_text))
    return results
from transformers import pipeline
pipe = pipeline(task='text-classification', model='SamLowe/roberta-base-go_emotions')


def analyze(text):
    # split text into chunks of <=512 tokens
    inputs = pipe.tokenizer(text, return_overflowing_tokens=True, max_length=512, truncation=True)
    print(inputs)
    results = []
    for input_ids in inputs["input_ids"]:
        chunk_text = pipe.tokenizer.decode(input_ids, skip_special_tokens=True)
        print(f'{chunk_text} ////')
        results.extend(pipe(chunk_text))
        print(results)
    return results
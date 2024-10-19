from datasets import load_dataset
ds = load_dataset("phucnv32/pho-gpt-preprocessed-datasets")
train_dataset = ds['train']
train_dataset.to_json("train.jsonl")
from transformers import GPT2Tokenizer , GPT2Config ,GPT2Model
from pathlib import Path
import pandas as pd 
import uuid


tokenizer = GPT2Tokenizer.from_pretrained("Open-Langbrot")

paths = [str(x) for x in Path(r'G:\gpt\data\clean_text').glob('*.txt')]

ids = []
texts = []

# Iterate through each text file
for path in paths:
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()

        # Generate a unique ID using uuid
        unique_id = str(uuid.uuid4())

        # Append data to lists
        ids.append(unique_id)
        texts.append(text)

# Create a DataFrame
df = pd.DataFrame({"Id": ids, "text": texts})
csv_file_path = 'khasi_.csv'  
df.to_csv(csv_file_path, index=False)


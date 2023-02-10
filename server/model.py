import torch
import os
from pathlib import Path
print(Path.joinpath(Path.cwd(),"tokenizer.pt"))

def summarizer(text):
    tokpath=Path.joinpath(Path.cwd(),"tokenizer.pt")
    modpath=Path.joinpath(Path.cwd(),"kobart.pt")
    tokenizer = torch.load(tokpath)
    model = torch.load(modpath)
    text = text.replace('\n', ' ')
    raw_input_ids = tokenizer.encode(text)
    input_ids = [tokenizer.bos_token_id] + raw_input_ids + [tokenizer.eos_token_id]
    summary_ids = model.generate(torch.tensor([input_ids]),  num_beams=4,  max_length=512,  eos_token_id=1)
    summed=tokenizer.decode(summary_ids.squeeze().tolist(), skip_special_tokens=True)
    return summed

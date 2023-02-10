import torch
def summarizer(text):
    tokenizer = torch.load('./server/tokenizer.pt')
    model = torch.load('./server/kobart.pt')
    text = text.replace('\n', ' ')

    raw_input_ids = tokenizer.encode(text)
    input_ids = [tokenizer.bos_token_id] + raw_input_ids + [tokenizer.eos_token_id]

    summary_ids = model.generate(torch.tensor([input_ids]),  num_beams=4,  max_length=512,  eos_token_id=1)
    summed=tokenizer.decode(summary_ids.squeeze().tolist(), skip_special_tokens=True)
    return summed

import flask
from flask import Flask, request, render_template
import torch 
#from transformers import PreTrainedTokenizerFast
#from transformers import BartForConditionalGeneration
app=Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return flask.render_template('index.html')
@app.route('/predict')
def make_prediction():
    
    text= request.values.get('text')

    tokenizer = torch.load('tokenizer.pt')
    model = torch.load('kobart.pt')
    text = text.replace('\n', ' ')
    raw_input_ids = tokenizer.encode(text)
    input_ids = [tokenizer.bos_token_id] + raw_input_ids + [tokenizer.eos_token_id]
    summary_ids = model.generate(torch.tensor([input_ids]),  num_beams=4,  max_length=512,  eos_token_id=1)
    summed=tokenizer.decode(summary_ids.squeeze().tolist(), skip_special_tokens=True)
    return render_template('index.html',label=summed)
if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)


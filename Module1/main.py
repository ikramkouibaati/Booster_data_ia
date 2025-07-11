from fastapi import FastAPI
from pydantic import BaseModel
from transformers import T5Tokenizer, T5ForConditionalGeneration

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API T5. Utilisez /predict avec POST."}


tokenizer = T5Tokenizer.from_pretrained("t5-small")
model = T5ForConditionalGeneration.from_pretrained("t5-small")

class TextRequest(BaseModel):
    text: str

@app.post("/predict")
def predict(req: TextRequest):
    input_ids = tokenizer.encode(req.text, return_tensors="pt")
    output_ids = model.generate(input_ids)
    output = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return {"output": output}

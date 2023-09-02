import pandas as pd
import dill
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

file_name = 'best_pipe.pkl'
with open(file_name, 'rb') as file:
   model = dill.load(file)
   
class Form(BaseModel):
    id: int
    device_brand: str
    device_browser: str
    device_category: str
    device_screen_resolution: str
    geo_city: str
    geo_country: str
    utm_adcontent: str
    utm_campaign: str
    utm_medium: str
    utm_source: str


class Prediction(BaseModel):
    id: int
    prediction: int

@app.get('/status')
def status():
    return "I'm OK"


@app.get('/version')
def version():
    return model['metadata']


@app.post('/predict', response_model=Prediction)
def predict(form: Form):
    df = pd.DataFrame.from_dict([form.model_dump()])
    y = model['model'].predict(df)
    return {'id': form.id, 'prediction': y[0]}


uvicorn.run(app, host="127.0.0.1", port=8000)
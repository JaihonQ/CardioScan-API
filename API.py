import uvicorn 
from pydantic import BaseModel
from fastapi import FastAPI
from typing import List
import numpy as np
import joblib

model = joblib.load('NeuralNetwork_Final_Model.pkl')

app = FastAPI()

class InputData(BaseModel):
    inputs: List[float]

@app.get('/')
def home():
    return {'message':'running system'}

@app.post('/predict')
def prediction(Inputs:InputData):
    result = model.predict_proba([Inputs.inputs])[0][1]
    reshape_inputs = np.array(result).reshape(-1, 1)
    return {'result':reshape_inputs.tolist()}


if __name__ == "__main__":
    uvicorn.run('API:app', reload=True , host='0.0.0.0', port=8000)


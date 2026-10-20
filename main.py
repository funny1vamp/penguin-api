
from fastapi.responses import FileResponse
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# 启动时加载一次模型
model = joblib.load("model.joblib")
app = FastAPI(title="Penguin species")

# 定义输入数据的格式
class Penguin(BaseModel):
    bill_length_mm: float
    bill_depth_mm: float
    flipper_length_mm: float
    body_mass_g: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(penguin: Penguin):
    # 将输入数据转成 DataFrame，并确保列名与训练时一致
    X = pd.DataFrame([penguin.model_dump()])
    prediction = model.predict(X)[0]
    return {"species": prediction}

@app.get("/")
def home(): 
    return FileResponse("index.html")
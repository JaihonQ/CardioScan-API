# CardioScan-API
AI-powered FastAPI system for predicting heart disease risk using machine learning (CardioScan).

❤️ CardioScan API

CardioScan is an AI-powered system for predicting heart disease risk using machine learning.
This API is built with FastAPI and allows real-time prediction using clinical input features.

---

🚀 Features

- Heart disease prediction using ML model
- FastAPI backend (fast and efficient)
- JSON-based API (easy integration with UI / Mobile / Web)
- Ready for deployment (Railway, Render, VPS)

---

🧠 Model

The model is trained using supervised machine learning on clinical health data such as:

- Age
- Cholesterol
- Blood Pressure
- Other medical features

---

📦 Requirements

Make sure you have Python installed, then install dependencies:

🔹 Required Libraries:

- fastapi
- uvicorn
- scikit-learn
- numpy
- joblib
- pydantic

🔹 Install all:

pip install fastapi uvicorn scikit-learn numpy joblib pydantic

---

▶️ Run the API

uvicorn API:app --host 0.0.0.0 --port 8000

Then open:

http://127.0.0.1:8000/docs

---

📡 API Endpoint

🔸 POST "/predict"

Request:

{
  "inputs": [feature1, feature2, feature3, ...]
}

Response:

{
  "result": 0.87
}

---

📁 Project Structure

cardioscan-api/
│
├── API.py
├── model.pkl
├── requirements.txt
├── README.md

---

🌐 Deployment

This API can be deployed on:

- Railway
- Render
- VPS

---

👨‍💻 Author

Developed by Jaihone Qayomi

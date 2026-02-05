# 🕵️ Agentic HoneyPot API

An **Agentic HoneyPot API** designed to detect, analyze, and respond to scam or phishing-style messages in real time. This API is built using **FastAPI**, secured with an **API key**, and supports **session-based conversation tracking** for realistic scam analysis.

This project is deployed on **Render** and submitted successfully for evaluation.

---

## 🚀 Live Deployment

* **Base URL**: [https://honeypot-ai-719x.onrender.com](https://honeypot-ai-719x.onrender.com)
* **API Endpoint**: `/api/honeypot`
* **Swagger Docs**: [https://honeypot-ai-719x.onrender.com/docs](https://honeypot-ai-719x.onrender.com/docs)

---

## 🔐 Authentication

All requests must include an API key via request headers:

```
x-api-key: sk_honeypot_2026_secret
```

Requests without a valid API key will be rejected.

---

## 📌 API Endpoint Details

### POST `/api/honeypot`

Analyzes a suspicious message and returns extracted intelligence.

#### Request Headers

```
Content-Type: application/json
x-api-key: sk_honeypot_2026_secret
```

#### Request Body (Required)

```json
{
  "session_id": "session-001",
  "message": "Your bank account will be blocked today. Click this link immediately."
}
```

| Field      | Type   | Description                                         |
| ---------- | ------ | --------------------------------------------------- |
| session_id | string | Unique session identifier for conversation tracking |
| message    | string | Incoming suspicious/scam message                    |

---

#### Successful Response (200)

```json
{
  "status": "success",
  "reply": "This message appears to be a phishing attempt impersonating a bank.",
  "turns": 1
}
```

---

#### Error Responses

##### 401 – Unauthorized

```json
{ "detail": "Invalid or missing API key" }
```

##### 422 – Validation Error

```json
{ "detail": "session_id and message are required" }
```

---

## 🧠 Key Features

* 🔑 API-key based authentication
* 🧵 Session-aware conversation tracking
* 🧪 Input validation using Pydantic
* ⚡ FastAPI for high performance
* ☁️ Cloud deployed on Render
* 📘 Interactive Swagger documentation

---

## 🛠 Tech Stack

* **Python 3.10+**
* **FastAPI**
* **Uvicorn**
* **Pydantic**
* **Render Cloud Platform**

---

## 📂 Project Structure

```
.
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ Running Locally

### 1️⃣ Clone the repository

```
git clone https://github.com/<your-username>/agentic-honeypot-api.git
cd agentic-honeypot-api
```

### 2️⃣ Create virtual environment

```
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run the server

```
uvicorn main:app --reload
```

Server will run at:

```
http://127.0.0.1:8000
```

---

## ☁️ Deployment on Render (Summary)

* Runtime: **Python**
* Start Command:

```
uvicorn main:app --host 0.0.0.0 --port $PORT
```

* Environment Variable:

```
API_KEY=sk_honeypot_2026_secret
```

---

## 🧾 Evaluation Readiness Checklist

* ✅ Public API endpoint
* ✅ API key authentication enabled
* ✅ Correct JSON request/response format
* ✅ Stable cloud deployment
* ✅ Swagger documentation accessible

---

## 👨‍💻 Author

* **Sumanth Nallajonnala**
* Built as part of the *Agentic HoneyPot API Challenge* 🚀

---

## 📄 License

This project is intended for educational and evaluation purposes only.

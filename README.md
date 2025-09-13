# 🚀 Free2GPT API Wrapper

This is a simple **Flask-based API wrapper** for [Free2GPT](https://chat2.free2gpt.com),  
hostable on **Vercel**. It lets you send messages via a simple GET request and receive an AI-generated reply in JSON format.

---

## 🔧 Features
- Simple REST API (GET request)
- Automatically generates required `sign` and `timestamp`
- Clean JSON response
- Deployable on **Vercel** instantly

---

## 📡 Usage

Once deployed on Vercel:

```
https://your-app.vercel.app/api/chat?text=Hello+Free2GPT
```

### ✅ Example Response
```json
{
  "reply": "Hello! How can I help you today? I'm here to assist with a wide range of tasks...",
  "api_by": "@DevZeron"
}
```

---

## 📂 Project Structure
```
├── api
│   └── chat.py       # Main API code
├── requirements.txt  # Dependencies
└── vercel.json       # Vercel configuration
```

---

## ⚙️ Installation & Deployment

### 1. Clone the repo
```bash
git clone https://github.com/CodeDevZeron/Gemini-Api.git
cd Gemini-Api
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run locally
```bash
python api/chat.py
```

### 4. Deploy on Vercel
```bash
vercel deploy --prod
```

---

## 👤 Developer Info
- **Name:** DevZeron  
- **Telegram:** [@DevZeron](https://t.me/DevZeron)  
- **Telegram Channel:** [CodeDevZeron](https://t.me/CodeDevZeron)

---

## ⭐ Credit
This API wrapper is developed and maintained by **DevZeron**.  
If you use it, please give proper credit 🙏

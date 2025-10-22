# Currency_convertor_chatbot
This is a basic chatbot that helps in currency exchange
# 💱 Dialogflow Currency Converter Chatbot

A smart currency conversion chatbot built using **Dialogflow**, **Flask**, and **ExchangeRate API**.  
The bot converts currencies in real time (like USD → INR, EUR → GBP, etc.) through natural conversations.

---

## 🚀 Features

- 🌍 Converts between **multiple global currencies** (USD, EUR, GBP, INR, JPY, CAD, etc.)
- 🤖 Integrated with **Dialogflow CX/ES** for natural language understanding
- 🔗 Uses **Flask** as a backend fulfillment webhook
- 💬 Real-time API calls via **ExchangeRate API**
- 🌐 Publicly accessible using **ngrok**
- ⚡ Returns accurate and instant conversion results

---

## 🧠 Tech Stack

| Component | Technology Used |
|------------|----------------|
| Frontend (Chat) | Dialogflow Console |
| Backend (Fulfillment) | Flask (Python) |
| API | [ExchangeRate API](https://www.exchangerate-api.com/) |
| Hosting (Tunnel) | ngrok |
| Language | Python 3.8+ |

---

## 📂 Project Structure

currency-converter-bot/
├── app.py # Flask fulfillment code

├── requirements.txt # Python dependencies

├── README.md # Project documentation

└── .gitignore

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/currency-converter-bot.git
cd currency-converter-bot

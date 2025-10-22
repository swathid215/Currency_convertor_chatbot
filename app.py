from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# 🔑 Your ExchangeRate API key
API_KEY = "c8c7b8e1451effefc73915cb"

@app.route("/", methods=["POST"])
def index():
    data = request.get_json(force=True)
    print("🔹 Incoming request:", data)

    try:
        params = data["queryResult"]["parameters"]

        # Source currency and amount
        source_currency = params["unit-currency"]["currency"].upper()
        amount = float(params["unit-currency"]["amount"])

        # Target currency (may be list like ["INR"])
        target_currency = params.get("currency-name", "")
        if isinstance(target_currency, list) and target_currency:
            target_currency = target_currency[0]
        target_currency = target_currency.upper()

        # Fetch conversion rate
        rate = fetch_conversion_factor(source_currency, target_currency)

        # Prepare response
        if rate == "LIMIT_REACHED":
            response_text = (
                "⚠️ Sorry, the currency conversion limit has been reached for today. "
                "Please try again tomorrow."
            )
        elif rate:
            final_amount = round(amount * rate, 2)
            response_text = (
                f"{amount} {source_currency} equals {final_amount} {target_currency}."
            )
        else:
            response_text = (
                "❌ Sorry, I couldn't fetch the exchange rate right now. "
                "Please try again later."
            )

    except Exception as e:
        print("❌ Error in processing:", e)
        response_text = "Something went wrong while processing your request."

    print("🔹 Response to Dialogflow:", response_text)
    return jsonify({"fulfillmentText": response_text})


def fetch_conversion_factor(source, target):
    """Fetch real-time conversion rate using ExchangeRate API with better error handling."""
    try:
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{source}/{target}"
        print(f"📡 Fetching URL: {url}")

        # Set timeout to avoid Dialogflow webhook timeout
        res = requests.get(url, timeout=5)
        data = res.json()
        print("📩 API Response:", data)

        # Check success
        if data.get("result") == "success":
            return data["conversion_rate"]

        # Handle known API errors
        error_type = data.get("error-type", "")
        if error_type == "quota-exceeded":
            print("⚠️ API quota exceeded.")
            return "LIMIT_REACHED"
        elif error_type == "invalid-key":
            print("⚠️ Invalid API key.")
            return None
        else:
            print("⚠️ Unknown API error:", error_type)
            return None

    except requests.Timeout:
        print("⏳ API request timed out.")
        return None
    except Exception as e:
        print("❌ Exception during API call:", e)
        return None


if __name__ == "__main__":
    # 👇 Run the app
    # Use 0.0.0.0 to expose it if deploying (for localhost just keep default)
    app.run(debug=True)

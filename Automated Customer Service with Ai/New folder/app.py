from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

DOMAIN_DATA = {
    "banking": {
        "balance": "You can check balance via ATM or mobile banking.",
        "loan": "We offer Home, Personal, and Education loans.",
        "card": "If card is lost, block it immediately.",
        "account": "Account verification is required."
    },
    "hospital": {
        "appointment": "Appointments can be booked online or offline.",
        "doctor": "Please specify the department.",
        "emergency": "Visit emergency ward immediately.",
        "report": "Reports are available after 24 hours."
    },
    "education": {
        "admission": "Admissions are currently open.",
        "course": "Engineering, Arts, Science courses available.",
        "exam": "Exams are semester-based.",
        "fees": "Fees depend on the selected course."
    },
    "ecommerce": {
        "order": "Provide order ID to track order.",
        "refund": "Refunds processed in 5–7 days.",
        "return": "Returns allowed within 10 days.",
        "delivery": "Delivery takes 3–5 days."
    },
    "it": {
        "login": "Check username and password.",
        "password": "Reset password using OTP.",
        "error": "Please share the error code.",
        "network": "Restart router to resolve network issues."
    }
}

def ai_response(domain, msg):
    msg = msg.lower()
    if msg in ["hi", "hello", "hey"]:
        return "Hello 👋 I'm your AI assistant. How can I help you?"
    if domain in DOMAIN_DATA:
        for key in DOMAIN_DATA[domain]:
            if key in msg:
                return DOMAIN_DATA[domain][key]
    return "Can you please explain your issue more clearly?"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    reply = ai_response(data['domain'], data['message'])
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)

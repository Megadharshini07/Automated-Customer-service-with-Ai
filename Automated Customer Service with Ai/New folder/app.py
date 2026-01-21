from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

DOMAIN_DATA = {
    "banking": {
        "balance": "You can check balance via ATM or mobile banking. Want steps?",
        "loan": "Home, Personal and Education loans available. Which one?",
        "card": "Lost card? Please block it immediately. Need guidance?",
        "account": "Account verification required. Savings or current account?"
    },
    "hospital": {
        "appointment": "Book appointment online or offline. Which do you prefer?",
        "doctor": "Please tell the department name.",
        "emergency": "Visit ER immediately or call ambulance.",
        "report": "Reports available after 24 hours."
    },
    "education": {
        "admission": "Admissions are open now. UG or PG?",
        "course": "Engineering, Arts, Science and Management courses available.",
        "exam": "Semester-wise exams conducted.",
        "fees": "Fees depend on course selection."
    },
    "ecommerce": {
        "order": "Please provide order ID to track order.",
        "refund": "Refunds processed within 5-7 days.",
        "return": "Returns accepted within 10 days.",
        "delivery": "Delivery in 3-5 working days."
    },
    "it": {
        "login": "Please verify username and password.",
        "password": "Reset password using OTP.",
        "error": "Please share error code.",
        "network": "Restart router to fix network issues."
    }
}

def ai_response(domain, message):
    msg = message.lower()
    if any(w in msg for w in ["hi", "hello", "hey"]):
        return "Hello! How can I help you today?"

    if domain in DOMAIN_DATA:
        for key, val in DOMAIN_DATA[domain].items():
            if key in msg:
                return val

    return "Sorry, I didn't understand. Please explain more."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    reply = ai_response(data['domain'], data['message'])
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)

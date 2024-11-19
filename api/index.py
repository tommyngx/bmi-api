from flask import Flask, jsonify, request

app = Flask(__name__)

# API Key cố định
API_KEY = "pikachu_attack"

@app.before_request
def authenticate():
    # Lấy API Key từ header
    api_key = request.headers.get("X-API-Key")
    if api_key != API_KEY:
        return jsonify({"error": "Unauthorized. Invalid API Key."}), 401

@app.route("/")
def home():
    return "Welcome to the BMI API. Use the `/api/bmi` endpoint with `weight` and `height` query parameters."

@app.route("/api/bmi", methods=["GET"])
def calculate_bmi():
    # Lấy tham số từ query
    weight = request.args.get("weight", type=float)
    height = request.args.get("height", type=float)

    # Kiểm tra dữ liệu
    if not weight or not height or height <= 0:
        return jsonify({"error": "Invalid input. Please provide valid weight and height."}), 400

    # Tính BMI
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"

    # Trả về kết quả
    return jsonify({
        "bmi": round(bmi, 2),
        "category": category
    })

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Endpoint not found."}), 404
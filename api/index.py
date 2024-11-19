from flask import Flask, jsonify, request

app = Flask(__name__)

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
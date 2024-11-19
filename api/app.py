from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate-bmi', methods=['POST'])
def calculate_bmi():
    try:
        # Lấy dữ liệu từ request
        data = request.get_json()
        weight = data.get("weight")
        height = data.get("height")

        # Kiểm tra dữ liệu hợp lệ
        if not weight or not height or height <= 0:
            return jsonify({"error": "Invalid input"}), 400

        # Tính toán BMI
        bmi = weight / (height ** 2)
        category = ""
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        # Trả kết quả
        return jsonify({
            "bmi": round(bmi, 2),
            "category": category
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/bmi', methods=['POST'])
def bmi():
    data = request.json
    height = data['height']
    weight = data['weight']
    result = calculate_bmi(height, weight)
    return jsonify({"bmi": result})

@app.route('/bmr', methods=['POST'])
def bmr():
    data = request.json
    height = data['height']
    weight = data['weight']
    age = data['age']
    gender = data['gender']
    result = calculate_bmr(height, weight, age, gender)
    return jsonify({"bmr": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

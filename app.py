from flask import Flask, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)
@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Calculateur de Santé</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #f0f0f0;
                margin: 0;
                padding: 20px;
            }
            .container {
                background: #fff;
                padding: 20px;
                margin: auto;
                max-width: 500px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
            }
            h1 {
                color: #333;
            }
            p {
                color: #666;
                margin-bottom: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Bienvenue sur le Calculateur de Santé</h1>
            <p>Utilisez l'API REST pour calculer votre IMC et votre Métabolisme de Base.</p>
            <p>Endpoints disponibles :</p>
            <ul>
                <li><b>/bmi</b> : Calcul de l'IMC (POST)</li>
                <li><b>/bmr</b> : Calcul du Métabolisme de Base (POST)</li>
            </ul>
        </div>
    </body>
    </html>
    '''
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
    app.run(host='0.0.0.0', port=5000, debug=True)

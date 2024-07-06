from flask import Flask, request, jsonify
from XGBoost_20240508_apiv2 import predict  # Asegúrate de que este es el nombre correcto

app = Flask(__name__) # definimos una instancia de Flask

@app.route('/predict', methods=['POST'])
def predict_temperature():
    data = request.get_json(force=True)  # Obtiene los datos de entrada del cliente
    medidas=json['medidas']
    reg=joblib.load(modelo_entrenado1305.pkl)
    #prediction = predict(data)  # Llama a la función de predicción de tu modelo
    prediccion=reg.predict(data)
    return jsonify({'prediction': prediction})  # Devuelve la predicción al cliente

if __name__ == '__main__':
    app.run() #debug=True,  host='200.58.107.20', port=2082

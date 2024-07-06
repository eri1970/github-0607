from flask import Flask, request, jsonify
import joblib  # Importa joblib para cargar el modelo

app = Flask(__name__)  # Definimos una instancia de Flask

# Asegúrate de incluir la ruta correcta y el nombre del archivo para el modelo entrenado
model_path = 'modelo_entrenado1305.pkl'

# Cargar el modelo una sola vez, no en cada llamada a la API para mejorar la eficiencia
model = joblib.load(model_path)

@app.route('/predict', methods=['POST'])
def predict_temperature():
    data = request.get_json(force=True)  # Obtiene los datos de entrada del cliente
    medidas = json['Medidas']
    
    # Asegúrate de que los datos que recibes están en el formato adecuado para el modelo
    # Aquí suponemos que data ya es un array o se necesita algún procesamiento para adecuarlo
    prediction = model.predict([data])  # Llama a la función de predicción de tu modelo

    # Devuelve la predicción al cliente
    return jsonify({'prediction': prediction})  # Usar .tolist() tolist para convertir arrays de NumPy a listas

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)


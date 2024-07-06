# Importar las bibliotecas necesarias
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
import plotly.graph_objects as go
import pandas as pd
import json

# Ruta al archivo JSON
json_file_path = 'e:/2024/databricks/notebook 25032024/XGBoost py/allinone20240505.json'


import pandas as pd
import json
from xgboost import XGBRegressor

# Ruta al archivo JSON
json_file_path = 'e:/2024/databricks/notebook 25032024/XGBoost py/allinone20240505.json'

# Lista para almacenar todos los objetos JSON
data_list = []

# Abrir y leer el archivo JSON línea por línea
with open(json_file_path, 'r') as file:
    for line in file:
        json_object = json.loads(line)
        data_list.append(json_object)

print(data_list)

def preprocess_data(data_list):
    df = pd.DataFrame(data_list)
    if 'temp' in df.columns:
        num_lags = 24  # Número de lags reducido
        for lag in range(1, num_lags + 1):
            df[f'lag_{lag}'] = df['temp'].shift(lag)
        df.fillna(df['temp'].mean(), inplace=True)  # Imputar los NaNs con la media de 'temp'
        X = df.drop('temp', axis=1)  # Características para la predicción
        y = df['temp']  # Valores reales para cálculo de RMSE
        return X, y
    else:
        return pd.DataFrame(), pd.Series()  # Devolver estructuras vacías si 'temp' no está disponible

# Suponemos que data_list ya está definido
data_list = [{'temp': i} for i in range(30)]  
preprocess_data(data_list)  # Llamada a la función

def predict(data_list):
    X, y_true = preprocess_data(data_list)
    if not X.empty:
        xgb_model = XGBRegressor()
        xgb_model.load_model("E:\\2024\\databricks\\notebook 25032024\\XGBoost py\\XGBoost0805v1.model")
        y_pred = xgb_model.predict(X)
        rmse = np.sqrt(mean_squared_error(y_true, y_pred))
        print(f"RMSE: {rmse}")
        return y_pred.tolist()
    else:
        print("No data to predict")
        return []

# Asumiendo que 'data_list' es adecuadamente definido y contiene suficientes datos
predictions = predict(data_list)

print(predictions)

with open("predictions.txt", "w") as f:
    for pred in predictions:
        f.write(f"{pred}\n")
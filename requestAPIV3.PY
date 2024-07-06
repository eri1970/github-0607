import requests

# URL de la API
url = '
'

# Datos a enviar, asegúrate de que coincidan con lo que espera el modelo
data = {
  "Medidas": [
    {"id": "tarjeta MOV", "temp": 17.00, "hum": 54.00, "mov": 1, "tm": "2023-11-25 19:49:16"},
    {"id": "tarjeta MOV", "temp": 17.00, "hum": 54.00, "mov": 0, "tm": "2023-11-25 19:54:18"}
  ]
}

# Enviar la solicitud POST
response = requests.post(url, json=data)

# Imprimir la respuesta del servidor
print(response.text)

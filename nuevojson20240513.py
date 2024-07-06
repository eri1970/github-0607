import json

# Ruta al archivo JSON
archivo_json = 'E:/2024/databricks/notebook 25032024/XGBoost py/API/allinone20240505.json'

# Leer y decodificar cada objeto JSON de una línea del archivo
datos = []
with open(archivo_json, 'r') as file:
    for line in file:
        try:
            objeto_json = json.loads(line)
            datos.append(objeto_json)
        except json.JSONDecodeError as e:
            print(f"Error al decodificar JSON en la línea: {line} - Error: {e}")

print(datos)

# Supongamos que datos_originales ya contiene una lista de diccionarios como los que mostraste
nuevos_datos = {"Medidas": archivo_json}

# Convertir los datos modificados de vuelta a JSON
json_data_modificado = json.dumps(nuevos_datos, indent=4)  # `indent=4` para una mejor legibilidad en el archivo
print(json_data_modificado)

# Guardar los nuevos datos JSON en un archivo
nuevo_archivo_json = 'datos_modificados.json'
with open(nuevo_archivo_json, 'w') as file:
    json.dump(nuevos_datos, file, indent=4)

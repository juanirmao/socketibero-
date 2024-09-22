# Importamos las librerías necesarias de Flask
from flask import Flask, request, jsonify

# Creamos una instancia de la aplicación Flask
app = Flask(__name__)

# Definimos una ruta que acepta solicitudes POST en '/send'
@app.route('/send', methods=['POST'])
def send_message():
    # Obtenemos los datos JSON enviados por el cliente
    data = request.json
    # Extraemos el mensaje del cuerpo de la solicitud
    message = data.get('message')
    # Creamos una respuesta que incluye el mensaje recibido
    response = f"Mensaje recibido: {message}"
    # Devolvemos la respuesta como JSON
    return jsonify({"response": response})

# Iniciamos la aplicación en modo de depuración
if __name__ == '__main__':
    app.run(debug=True)

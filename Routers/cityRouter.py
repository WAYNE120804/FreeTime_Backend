from flask import Blueprint, request, jsonify
from Controllers.cityController import add_city

# Crear el blueprint para las rutas de 'city'
city_router = Blueprint('city_router', __name__)

# Ruta para agregar una ciudad
@city_router.route('/agregar_city', methods=['POST'])
def add_city_route():
    data = request.json
    city_name = data.get('city_name')
    state_id = data.get('state_id')

    if not city_name or not state_id:
        return jsonify({"error": "Faltan datos"}), 400

    response = add_city(city_name, state_id)
    if(response != None):
        return jsonify({"message": f"Ciudad {city_name} agregada exitosamente"}), 201
    else:
        return jsonify({"message": f"Error al agregar la ciudad"}), 404
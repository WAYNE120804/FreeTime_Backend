from DataBase.connection import getConnection

def add_city(city_name, state_id):
    connection = getConnection()
    cursor = connection.cursor()

    # Crear la query para insertar una nueva ciudad
    query = """
        INSERT INTO city (city_name, state_id)
        VALUES (%s, %s)
    """
    
    try:
        # Ejecutar la query con los parámetros
        cursor.execute(query, (city_name, state_id))
        connection.commit()
        print(f"Ciudad {city_name} agregada exitosamente.")
        return city_name
    except Exception as e:
        print(f"Error al agregar la ciudad: {e}")
        connection.rollback()
        return
    finally:
        cursor.close()
        connection.close()
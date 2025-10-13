#abro pi_digits.txt y le damos el nombre de file_object puse al path completo para que lo pueda correr desde donde sea en la terminal
#si no lo pongo completo tengo que abrir esa carpeta en la terminal
#tambien se puede poner en una variable

filepath = '/workspaces/Learning_algorithms/python_crash_course/files_and_exceptions/pi_digits.txt'
with open(filepath) as file_object:
    #guardo en contents el resultado de leer file_object
    contents = file_object.read()
    #Quito el espacio en blanco de la derecha
    print(contents.rstrip())


import sqlite3
import time

# Conexión a la base de datos
try:
    conexion = sqlite3.connect("mi_base.db")  # Cambia esto si usas otro motor
    cursor = conexion.cursor()

    # Leer archivo línea por línea con pausa
    with open("datos.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            tray_id = linea.strip()
            if tray_id:
                try:
                    query = """
                        SELECT * FROM slot_contents
                        WHERE scnt_slot_tray_id = ? AND scnt_quantity = 0
                    """
                    cursor.execute(query, (tray_id,))
                    resultado = cursor.fetchall()
                    if resultado:
                        print(f"✔️ {tray_id}: {len(resultado)} resultado(s)")
                        for fila in resultado:
                            print(fila)
                    else:
                        print(f"❌ {tray_id}: sin resultados")
                except Exception as e:
                    print(f"⚠️ Error al consultar {tray_id}: {e}")
                time.sleep(5)  # Pausa de 5 segundos entre cada consulta

except Exception as e:
    print(f"🚨 Error al conectar con la base de datos o abrir el archivo: {e}")

finally:
    try:
        if conexion:
            conexion.close()
            print("🔒 Conexión cerrada correctamente.")
    except Exception as e:
        print(f"⚠️ Error al cerrar la conexión: {e}")

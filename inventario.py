# Definir funciones para llamar desde el menu

# Importamos librerias a usar (usaremos un archivo json para guardar los datos)
import json, os

# Variable que guarda el nombre del archivo json
DATA_FILE = "data.json"

# Definimos la funcion que nos permitira cargar los datos al archivo json
def cargar_datos():
    if not os.path.exists(DATA_FILE):
        return  []
    
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return[]
        
# Definimos la funcion para guardar los datos al archivo json
def guardar_datos(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        
# Definimos la funcion para agregar productos, que solicitara los datos del producto al usuario
def agregar_producto(nombre, cantidad, precio_unitario):
    data = cargar_datos()

    producto = {
        "id" : len(data) + 1,
        "nombre" : nombre,
        "cantidad" : cantidad,
        "precio_unitario" : precio_unitario
    }
    data.append(producto)
    guardar_datos(data)

    return True

# Definimos la funcion para listar todos los productos que se encuentran agregados al archivo json
def listar_producto():
    return cargar_datos()

# Definimos la funcion para buscar un producto por su nombre
def buscar_producto(busqueda):
    data = cargar_datos()
    return [p for p in data 
            if busqueda.lower()
            in p["nombre"].lower()]

# Definimos la funcion para eliminar un producto segun su ID
def eliminar_producto(product_id):
    data = cargar_datos()
    nueva_lista = [p for p in data
                   if p["id"] != product_id]
    
    if len(data) == len(nueva_lista):
        return False
    
    guardar_datos(nueva_lista)
    return True
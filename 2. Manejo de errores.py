#2. Manejo de errores
#Uso un get para manejar errores más sencillos y una función para
#que el código sea más legible

def acceso_clave(diccionario, clave):
    return diccionario.get(clave, "Clave no encontrada")
    
computador = {
    "marca": "Asus",
    "procesador": "Intel Core i7",
    "ram": "8GB",
    "disco": "SSD 1TB"}

valor = acceso_clave(computador, "modelo")
print(valor)
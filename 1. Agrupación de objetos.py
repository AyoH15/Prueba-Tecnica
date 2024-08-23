#1. Agrupación de objetos
def agrupar_productos(lista_productos):
    agrupacion = {}
    i = 0

    for producto in lista_productos:
        i += 1
        fabricante = producto["Fabricante"]
        categoria = producto["Categoría"]
        genero = producto["Género"]
        producto[''] = f"Producto {i}"
        
        if fabricante not in agrupacion:
            agrupacion[fabricante] = {}
            
        if categoria not in agrupacion[fabricante]:
            agrupacion[fabricante][categoria] = {}
            
        if genero not in agrupacion[fabricante][categoria]:
            agrupacion[fabricante][categoria][genero] = [f"Producto {i}"]
        
    return agrupacion
        

producto_1 = {
    "Nombre": "Zapatos XYZ",
    "Código de barras": 8569741233658,
    "Fabricante": "Deportes XYZ",
    "Categoría": "Zapatos",
    "Género": "Masculino"
}

producto_2 = {
    "Nombre": "Zapatos ABC",
    "Código de barras": 7452136985471,
    "Fabricante": "Deportes XYZ",
    "Categoría": "Zapatos",
    "Género": "Femenino"
}

producto_3 = {
    "Nombre": "Camisa DEF",
    "Código de barras": 5236412896324,
    "Fabricante": "Deportes XYZ",
    "Categoría": "Camisas",
    "Género": "Masculino"
}

producto_4 = {
    "Nombre": "Bolso KLM",
    "Código de barras": 5863219635478,
    "Fabricante": "Carteras Hi-Fashion",
    "Categoría": "Bolsos",
    "Género": "Femenino"
}

lista_productos = [producto_1,producto_2,producto_3,producto_4]
resultado = agrupar_productos(lista_productos)
print(resultado)
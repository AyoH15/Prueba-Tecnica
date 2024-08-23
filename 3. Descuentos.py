#3. Ejercicio
def calcular_descuento(total_venta):
    if total_venta < 100:
        return 0
    elif total_venta >= 100 and total_venta <= 500:
        return 0.05
    else:
        return 0.1
    
total_venta = 500
descuento = calcular_descuento(total_venta)
nuevo_total = (1-descuento) * total_venta

print(f"Su descuento es del {descuento*100}%")
print(f"El precio total es de ${nuevo_total}")

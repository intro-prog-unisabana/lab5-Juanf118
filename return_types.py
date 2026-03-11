def obtener_precio_usuario():
    """Función para obtener el precio del usuario y convertirlo a un número"""
    preciostr = input("Ingrese el precio del producto:\n")
    return float(preciostr)
precio = obtener_precio_usuario()
print(precio)

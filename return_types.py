def obtener_precio_usuario() -> float:
    precio_str = input("Enter the item's price:\n")
    # Verificamos si el texto contiene solo números (o un punto decimal)
    if precio_str.replace(".", "", 1).isdigit():
        return float(precio_str)  # Aquí sí lo convertimos a número
    else:
        mensaje_error = "el valor ingresado no es válido es un texto: " + precio_str
        return mensaje_error

precio = obtener_precio_usuario()
print(precio)  # If the user enters 25, the output will be 25.0
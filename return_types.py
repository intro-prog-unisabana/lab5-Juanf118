def obtener_precio_usuario():
    """Solicita al usuario que ingrese el precio de un artículo y devuelve ese valor como un número de punto flotante."""
    entrada = input("Enter the item's price:\n")
    return float(entrada)
if __name__ == "__main__":
    print(obtener_precio_usuario())
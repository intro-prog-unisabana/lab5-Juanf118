def celsius_to_fahrenheit(temp):
    """
    Convierte una temperatura de Celsius a Fahrenheit.
    Firma: (float o int) -> float
    """
    # Aplicamos la fórmula matemática
    fahrenheit = (temp * 9/5) + 32
    
    # Retornamos el valor (sin imprimir nada dentro de la función)
    return float(fahrenheit)

# --- Pruebas de validación ---
if __name__ == "__main__":
    print(celsius_to_fahrenheit(0))    # Salida esperada: 32.0
    print(celsius_to_fahrenheit(100))  # Salida esperada: 212.0
    print(celsius_to_fahrenheit(-40))  # Salida esperada: -40.0
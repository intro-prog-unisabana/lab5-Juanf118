def celsius_to_fahrenheit(temp):
    """
    Convierte una temperatura de Celsius a Fahrenheit.
    Firma: (float o int) -> float
    """
    fahrenheit = (temp * 9/5) + 32
    
    return float(fahrenheit)

# --- Pruebas de validación ---
if __name__ == "__main__":
    print(celsius_to_fahrenheit(0))    
    print(celsius_to_fahrenheit(100))  
    print(celsius_to_fahrenheit(-40))  
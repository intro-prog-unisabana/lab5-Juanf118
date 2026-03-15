# 1. Importar la función desde el módulo proporcionado
from mystery_module import transform_data

def main():
    # 2. Solicitar datos al usuario para que no estén hardcoded
    # Convertimos x a entero y y a decimal (float) para cumplir la firma
    x = int(input("Enter value for x (int):\n"))
    y = float(input("Enter value for y (float):\n"))
    
    # El ejercicio pedía específicamente la cadena "quiz_test" para z
    z = "quiz_test"

    # 3. Llamar a la función respetando el contrato (firma)
    # def transform_data(x: int, y: float, z: str) -> float
    result = transform_data(x, y, z)

    # 4. Imprimir el valor de retorno
    print(result)

if __name__ == "__main__":
    main()


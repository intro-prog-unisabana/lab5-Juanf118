# 1. Importar la función desde el módulo proporcionado
from mystery_module import transform_data

def main():
    # Definir las variables según las instrucciones
    # (Asumiendo que x e y vienen de algún input o son fijos)
    x = 10
    y = 5.5
    z = "quiz_test"

    # 2. Llamar a la función usando la firma requerida
    # x: int, y: float, z: str
    result = transform_data(x, y, z)

    # 3. Imprimir el valor de retorno
    print(result)

if __name__ == "__main__":
    main()
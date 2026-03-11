def list_shift(lst, value):
    """Modificar una lista sumando un valor a cada elemento."""
    entrada = float (lst[0])
    for i in range(len(lst)):
        lst[i] += value
    return (lst)
print(list_shift([1, 2, 3], 5))

def calc_avg():
    """Solicita al usuario que ingrese tres números y devuelve el promedio de esos números."""
    entrada = input("Enter three numbers separated by spaces:\n")
    numeros = [float(num) for num in entrada.split()]
    return sum(numeros) / len(numeros)
print(calc_avg())

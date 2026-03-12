def list_shift(lst, value):
    """Modificar una lista sumando un valor a cada elemento."""
    entrada = float (lst[0])
    for i in range(len(lst)):
        lst[i] += value
    return (lst)
print(list_shift([1, 2, 3], 5))

def calc_avg():
    """Calcular el promedio de una lista de números."""
    lst = [1, 2, 3, 4, 5]
    total = sum(lst)
    avg = total / len(lst)
    return avg

def print_normalized():
    """Imprimir los números normalizados de una lista."""
    lst = [1, 2, 3, 4, 5]
    avg = calc_avg()
    normalized = [x - avg for x in lst]
    print(normalized)
def list_shift(lst, value):
    """Modificar una lista sumando un valor a cada elemento."""
    entrada = float (lst[0])
    for i in range(len(lst)):
        lst[i] += value
    return (lst)
print(list_shift([1, 2, 3], 5))
datos = [10, 20, 30, 40, 50]
def calc_avg(datos):
    if len(datos) == 0:
        return 0.0
    return sum(datos) / len(datos)

def list_shift(datos, shift_amount):
    for i in range(len(datos)):
        datos[i] = datos[i] + shift_amount

def print_normalized(datos):
    if len(datos) == 0:
        print("The list is empty.")
        return
    print(datos)
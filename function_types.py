datos = [2.0, 4.0, 6.0, 8.0]
def calc_avg(datos):
    if len(datos) == 0:
        return 0.0
    return sum(datos) / len(datos)
prom = calc_avg(datos)


def list_shift(datos, shift_amount):

    #print("Shift amount:", shift_amount)
    shifted_list = []
    for i in range(len(datos)):
        #print(f"Original value at index {i}: {datos[i]}")
        shifted_list.append(datos[i] + shift_amount)
        #print(f"Shifted value at index {i}: {shifted_list[i]}")
    #shifted_list = datos[1:] + [shift_amount]
    return shifted_list
#asignar el resultado de la funcion list_shift a una variable
lista = list_shift(datos, -prom)

def print_normalized(datos):
    if len(datos) == 0:
        print("The list is empty.")
        return
    print (datos)

imprimir = print_normalized(lista)
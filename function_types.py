##Lista original
datos = [2.0, 4.0, 6.0, 8.0]

#funcion para calcular el promedio de una lista de numeros
def cacl_avg(datos):
    if len(datos) == 0:
        return 0.0
    total = sum(datos)
    promedio = total / len(datos)
    return promedio
#asignar el resultado de la funcion calcular promedio a una variable
prom = cacl_avg(datos)

#funcion para desplazar los elementos de una lista por un valor dado
def list_shift(datos, shift_amount):
    if len(datos) == 0:
        return []
    #print("Shift amount:", shift_amount)
    shifted_list = []
    for i in range(len(datos)):
        #print(f"Original value at index {i}: {datos[i]}")
        shifted_list.append(datos[i] + shift_amount)
        #print(f"Shifted val ue at index {i}: {shifted_list[i]}")
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
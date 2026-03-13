import os
from math import *
directorio = os.getcwd()
print("Current working directory:",directorio)
entrada = (int(input("Enter an integer: ")))
valor_log = log2(entrada)
print("Log base 2 of", entrada, "is:", valor_log)
val_piso = floor(valor_log)
val_techo = ceil(valor_log)
print("Floor:", val_piso)
print("Ceiling:", val_techo)
x = 10
y = "hola"
def set_globals():
   """almacenar los globales"""
   globales = x, y
   
def get_globals():
    tupla = (x, y)
    print(tupla)
    return tupla
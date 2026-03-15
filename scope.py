int_global = None
str_global = None

def set_globals(some_int, some_str):
    global int_global
    global str_global
    int_global = some_int
    str_global = some_str
set_globals(10, "Hola") == int_global == 10 and str_global == "Hola"

def get_globals():
    return (int_global, str_global)
print(get_globals())
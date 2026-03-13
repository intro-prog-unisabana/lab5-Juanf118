flotantes = [1.5, 2.3, 3.7, 4.1, 5.6]
float = 2.0
def list_shift():
    for x in range(len(flotantes) - 1):
        flotantes[x] = flotantes[x + int(float)]

def calc_avg(flotantes):
    return sum(flotantes) / len(flotantes)
calc_avg(flotantes)
print(calc_avg(flotantes))
def print_normalized(calc_avg):
    return calc_avg
print(print_normalized(calc_avg(flotantes)))
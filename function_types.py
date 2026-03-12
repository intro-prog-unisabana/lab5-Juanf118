numbers = [1.5, 2.5, 3.5]
def calc_avg(numbers):
    total = sum(numbers)
    count = len(numbers)
    avg = total / count
    return avg
def list_shift(numbers, value):
    shifted_list = [num + value for num in numbers]
    return shifted_list
def print_normalized(numbers):
    total = sum(numbers)
    if total == 0:
        print("Cannot normalize an empty list or a list with all zeros.")
        return
    normalized = [num / total for num in numbers]
    print(normalized)

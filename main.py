import utils_calc
def main():
    while True:
        op = input("Which calculation would you like to perform (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):\n").strip().lower()
        if op == "exit":
            break
        valid_ops = ["add", "subtract", "multiply", "divide", "exponent", "modulo", "floor_divide", "absolute"]
        if op not in valid_ops:
            print("Invalid option!")
            continue
        if op == "absolute":
            num = float(input("Enter the number:\n"))
            result = utils_calc.absolute(num)
            print(f"The result is: {result}")
        else:
            num1 = float(input("Enter the first number:\n"))
            num2 = float(input("Enter the second number:\n"))
            if op == "add":
                result = utils_calc.add(num1, num2)
            elif op == "subtract":
                result = utils_calc.sub(num1, num2)
            elif op == "multiply":
                result = utils_calc.multiply(num1, num2)
            elif op == "divide":
                result = utils_calc.divide(num1, num2)
            elif op == "exponent":
                result = utils_calc.exponent(num1, num2)
            elif op == "modulo":
                result = utils_calc.modulo(num1, num2)
            elif op == "floor_divide":
                result = utils_calc.floor_divide(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print(f"The result is: {result}")
if __name__ == "__main__":
    main()
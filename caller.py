from mystery_module import transform_data

def main():
    x = int(input("Enter value for x (int):\n"))
    y = float(input("Enter value for y (float):\n"))
    z = "quiz_test"

    result = transform_data(x, y, z)
    print(result)

if __name__ == "__main__":
    main()


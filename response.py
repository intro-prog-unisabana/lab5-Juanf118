def input_response(generate_value, user_input):
    if user_input < generate_value:
        return "Too low! Try a higher number.", False
    elif user_input > generate_value:
        return "Too high! Try a lower number.", False
    else:
        return "Conrrect! You guessed the number!", True
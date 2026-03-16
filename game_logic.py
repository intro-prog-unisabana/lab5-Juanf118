import secret_number
import response
def run_game():
    seed = int(input("Enter a seed value: \n"))
    secret_number.seed_secret_number(seed)
    
    target = secret_number.generate_secret_number(1, 100)
    attempts = 0
    solved = False
    while not solved:
        guess = int(input("What is your guess: \n"))
        attempts += 1

        message, solved = response.input_response(target, guess)
        print(message)

    print(f"It took you {attempts} tries!.")
if __name__ == "__main__":
    run_game()
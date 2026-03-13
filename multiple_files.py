from utils import *
mensaje = input("Please type your message\n")
flip = flip(mensaje)
count_letters = count_letters(mensaje, "a")
encoded_message = (f"Your encoded message is:{flip}{count_letters}")
print(encoded_message)
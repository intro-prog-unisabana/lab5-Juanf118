import random
def seed_secret_number(seed):
    random.seed(seed)
def generate_secret_number(start, end):
    return random.randint(start, end)
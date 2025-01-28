import random
from api.constants import numbers, symbols, alphabet, alphabet_lowercase


def password_generator(l):
    password_length = l
    converted_password_length = int(password_length)
    all_symbols = [numbers, symbols, alphabet, alphabet_lowercase]
    flatted_list = [item for sublist in all_symbols for item in sublist]
    random.shuffle(all_symbols)
    password = []

    for i in range(converted_password_length):
        s = random.choice(flatted_list)
        password.append(s)
    final_password = "".join(password)
    return final_password






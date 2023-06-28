import random
import string

random.seed()


def generate_password(security: int = 1) -> str:
    if security == 0:
        password = "".join(random.choices(string.ascii_letters + string.digits, k=8))
    elif security == 1:
        password = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=12))
    elif security == 2:
        password = "".join(
            random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits + '!?*&$', k=12))
    else:
        password = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits + '!?*&$',
                                          k=4 * security))
    return str(password)


def generate_number(digits: int) -> int:
    number = "".join(random.choices(string.digits, k=digits))
    return int(number)


def generate_arithmetic_progression(first_term: int = 1, diff: int = 1, number_of_terms: int = 10) -> list:
    prog = []
    for i in range(1, number_of_terms + 1):
        prog.append(first_term + (i - 1) * diff)
    return prog


def n_term_arithmetic_progression(first_term: int = 1, diff: int = 1, n: int = 1) -> int:
    n_term =  first_term + (n - 1) * diff
    return n_term

def generate_geometric_progression(first_term: int = 1, q: int = 2, number_of_terms: int = 10) -> list:
    prog = []
    for i in range(number_of_terms):
        prog.append(first_term * q ** i)
    return prog

def n_term_geometric_progression(first_term: int = 1, q: int = 2, n: inr = 1) -> list:
    n_term = first_term * q ** (n - 1)
    return n_term

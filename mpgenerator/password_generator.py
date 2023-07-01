import random
import string
from math import log, e
from fractions import Fraction

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


def generate_arithmetic_progression(first_term: int = 1, step: int = 1, number_of_terms: int = 10) -> list:
    prog = []
    for i in range(1, number_of_terms + 1):
        prog.append(first_term + (i - 1) * step)
    return prog


def n_term_arithmetic_progression(first_term: int = 1, step: int = 1, n: int = 1) -> int:
    n_term = first_term + (n - 1) * step
    return n_term


def n_term_sum_arithmetic_progression(first_term: int = 1, step: int = 1, number_of_terms=10) -> float:
    sum = number_of_terms * (first_term + n_term_arithmetic_progression(first_term, step, number_of_terms)) / 2
    return sum


def generate_geometric_progression(first_term: int = 1, q: int = 2, number_of_terms: int = 10) -> list:
    prog = []
    for i in range(number_of_terms):
        prog.append(first_term * q ** i)
    return prog


def n_term_geometric_progression(first_term: int = 1, q: int = 2, n: int = 1) -> list:
    n_term = first_term * q ** (n - 1)
    return n_term


def n_term_sum_geometric_progression(first_term: int = 1, q: int = 2, number_of_terms: int = 10) -> int:
    sum = (first_term * (q ** number_of_terms - 1)) / (q - 1)
    return sum


def generate_harmonic_progression(first_term: int = 1, step=1, number_of_terms: int = 10) -> list:
    prog = []
    for i in range(1, number_of_terms + 1):
        term = Fraction.from_float(1 / (first_term + (i - 1) * step)).limit_denominator(first_term + (i - 1) * step)
        prog.append(str(term))
    return prog


def n_term_harmonic_progression(first_term: int = 1, step: int = 1, n: int = 10):
    n_term = Fraction(1, first_term + (n - 1) * step)
    return n_term


def n_terms_sum_harmonic_progression(first_term: int = 1, step: int = 1, number_of_terms: int = 5):
    sum = (1 / step) * log((2 * first_term + (2 * number_of_terms - 1) * step) / (2 * first_term - step), e)
    return sum

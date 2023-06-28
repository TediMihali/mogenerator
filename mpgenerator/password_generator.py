import random
import string

random.seed()


def generate_password(security: int = 1) -> str:
    if security == 0:
        password = "".join(random.choices(string.ascii_letters + string.digits, k=8))
    elif security == 1:
        password = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=12))
    else:
        password = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=4 * security))
    return str(password)


def generate_number(digits: int) -> int:
    number = "".join(random.choices(string.digits, k = digits))
    return int(number)

print(generate_number(5))
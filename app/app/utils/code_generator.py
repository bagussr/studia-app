import random
import string


def randomword_10():
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(10))


def randomword_15():
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(15))


def randomword_20():
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(20))

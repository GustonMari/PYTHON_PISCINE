import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k = 15))

# ! https://realpython.com/python-data-classes/
@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    # ! attention tres gros probleme ici si on utilise pas lambda on ne peut pas avoir de valeur par defaut
    # ! https://stackoverflow.com/questions/52063759/passing-default-list-argument-to-dataclasses
    login: str = field(default_factory = lambda: "Eagle", init = False)
    id: str = field(default_factory = generate_id, init = False)

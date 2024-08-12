import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generate a random 15-character string consisting
    of lowercase ASCII letters.

    Returns:
        str: A randomly generated 15-character string.
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student():
    """
    A class representing a student with a unique ID, login, and active status.

    Attributes:
        name (str): The first name of the student.
        surname (str): The last name of the student.
        id (str): A unique identifier for the student, automatically generated.
        login (str): The login name for the student, generated from the first
        letter of the name and the surname.
        active (bool): The active status of the student, default is True.
    """
    name: str
    surname: str
    id: str = field(init=False, default_factory=generate_id)
    login: str = field(init=False)
    active: bool = field(default=True)

    def __post_init__(self):
        """
        Post-initialization method to generate the unique ID and login name
        for the student after the initial creation of the instance.
        """
        self.login = self.name[0] + self.surname

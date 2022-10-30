from abc import abstractmethod, ABC
import re


class Pessoa(ABC):
    def __init__(self, email: str, fone: str):
        # mover estas validações para a tela depois.
        if re.match(r'^[-\w\.]+@([\w-]+\.)+[\w-]{2,4}$', email):
            self.__email = email
        else:
            raise EmailInvalidoException
        if re.match(r'^\(?[1-9]{2}\)? ?(?:[2-8]|9[1-9])[0-9]{3}\-?\s*?[0-9]{4}$', fone):
            self.__fone = fone
        else:
            raise FoneInvalidoException

    @abstractmethod
    def cadastro(self):
        ...

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        if isinstance(email, str):
            self.__email = email

    @property
    def fone(self):
        return self.__fone

    @fone.setter
    def fone(self, fone: str):
        if isinstance(fone, str):
            self.__fone = fone

class EmailInvalidoException(BaseException):
    ...

class FoneInvalidoException(BaseException):
    ...

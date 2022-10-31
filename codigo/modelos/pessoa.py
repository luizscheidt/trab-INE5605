from abc import abstractmethod, ABC


class Pessoa(ABC):
    def __init__(self, email: str, fone: str):
        self.__email = email
        self.__fone = fone

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

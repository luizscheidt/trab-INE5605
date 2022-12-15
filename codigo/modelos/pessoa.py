from abc import abstractmethod, ABC


class Pessoa(ABC):
    @abstractmethod
    def __init__(self, email: str, fone: str):
        self.__email = email
        self.__fone = fone
        self.__conta = None

    @abstractmethod
    def cadastro(self):
        ...

    @abstractmethod
    def representacao(self):
        ...

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def fone(self):
        return self.__fone

    @fone.setter
    def fone(self, fone: str):
        self.__fone = fone

    @property
    def conta(self):
        return self.__conta

    @conta.setter
    def conta(self, conta):
        self.__conta = conta


class EmailInvalidoException(BaseException):
    ...

class FoneInvalidoException(BaseException):
    ...

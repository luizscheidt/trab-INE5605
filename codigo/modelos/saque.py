from .data import Data
from .conta_corrente import ContaCorrente

class Saque:
    def __init__(self, id: int, valor: float, conta: ContaCorrente, data: Data):
        self.__id = id
        self.__valor = valor
        self.__conta = conta
        self.__data = data
        self.__tipo = 'saque'

    @property
    def id(self):
        return self.__id

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: Data):
        self.__data = data

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor: float):
        self.__valor = valor

    @property
    def conta(self):
        return self.__conta

    @conta.setter
    def conta(self, conta: float):
        self.__conta = conta

    @property
    def tipo(self):
        return self.__tipo

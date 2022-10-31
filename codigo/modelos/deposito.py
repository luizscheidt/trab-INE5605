from data import Data
from conta_corrente import ContaCorrente

class Deposito:
    def __init__(self, valor: float, conta: ContaCorrente, data: Data):
        self.__valor = valor
        self.__conta = conta
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
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: Data):
        self.__data = data

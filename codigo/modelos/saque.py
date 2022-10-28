from data import Data
from conta_corrente import ContaCorrente

class Saque:
    def __init__(self, valor: float, conta: ContaCorrente):
        self.__valor = valor
        self.__conta = conta

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor: float):
        self.__valor = valor 


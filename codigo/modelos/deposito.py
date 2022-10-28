from data import Data
from conta_corrente import ContaCorrente

class Deposito:
    def __init__(self, valor: float, conta: ContaCorrente):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor: float):
        self.__valor = valor 

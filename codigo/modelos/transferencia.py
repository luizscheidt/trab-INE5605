from .data import Data
from .conta_corrente import ContaCorrente

class Transferencia:
    def __init__(self, id: int, origem: ContaCorrente, destino: ContaCorrente, valor: float, data: Data):
        self.__valor = valor
        self.__origem = origem
        self.__destino = destino
        self.__data = data
        self.__id = id

    @property
    def origem(self):
        return self.__origem

    @origem.setter
    def origem(self, origem: ContaCorrente):
        self.__origem = origem

    @property
    def destino(self):
        return self.__destino

    @destino.setter
    def destino(self, destino: ContaCorrente):
        self.__destino = destino

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor: float):
        self.__valor = valor

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: float):
        self.__data = data

    @property
    def id(self):
        return self.__id

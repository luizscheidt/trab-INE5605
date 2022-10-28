from data import Data
from conta_corrente import ContaCorrente

class Transferencia:
    def __init__(self, origem: ContaCorrente, destino: ContaCorrente, valor: float):
        self.__valor = valor
        self.__origem = origem
        self.__destino = destino

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
        def valor(valor, valor: float):
            self.__valor = valor

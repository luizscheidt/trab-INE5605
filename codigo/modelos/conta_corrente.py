from modelos.pessoa import Pessoa

class ContaCorrente:

    def __init__(self, dono: Pessoa, numero: int, saldo: int = 0):
        self.__dono = dono
        self.__numero = numero
        self.__saldo = saldo
        self.__transferencias = []

    @property
    def dono(self):
        return self.__dono

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    @property
    def transferencias(self):
        return self.__transferencias

    @dono.setter
    def dono(self, dono: Pessoa):
        self.__dono = dono

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    @transferencias.setter
    def transferencias(self, transferencias):
        self.__saldo = transferencias

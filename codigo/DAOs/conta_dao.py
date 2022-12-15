from DAOs.dao import DAO
from modelos.conta_corrente import ContaCorrente

class ContaDAO(DAO):
    def __init__(self):
        super().__init__('contas.pkl')

    def add(self, conta: ContaCorrente):
        if conta and isinstance(conta, ContaCorrente) and isinstance(conta.numero, int):
            super().add(conta.numero, conta)

    def get(self, numero: int):
        if isinstance(numero, int):
            return super().get(numero)

    def remove(self, numero: int):
        if isinstance(numero, int):
            return super().remove(numero)

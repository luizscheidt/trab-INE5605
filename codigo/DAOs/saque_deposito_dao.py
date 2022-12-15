from DAOs.dao import DAO
from modelos.saque import Saque
from modelos.deposito import Deposito

class SaqueDepositoDAO(DAO):
    def __init__(self):
        super().__init__('saque_deposito.pkl')

    def add(self, operacao):
        if operacao and (isinstance(operacao, Saque) or isinstance(operacao, Deposito)) and isinstance(operacao.id, int):
            super().add(operacao.id, operacao)

    def get(self, id: int):
        if isinstance(id, int):
            return super().get(id)

from DAOs.dao import DAO
from modelos.transferencia import Transferencia

class TransferenciaDAO(DAO):
    def __init__(self):
        super().__init__('transferencias.pkl')

    def add(self, transferencia: Transferencia):
        if transferencia and isinstance(transferencia, Transferencia) and isinstance(transferencia.id, int):
            super().add(transferencia.id, transferencia)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

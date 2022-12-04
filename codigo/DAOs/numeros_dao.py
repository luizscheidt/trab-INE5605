from DAOs.dao import DAO

class NumeroDAO(DAO):
    def __init__(self):
        super().__init__('numeros.pkl')

    def add(self, tipo: str, numero):
        if tipo and isinstance(tipo, str) and isinstance(numero, int):
            super().add(tipo, numero)

    def get(self, tipo: str):
        if isinstance(tipo, str):
            numero = super().get(tipo)
            if not numero:
                self.add(tipo, 0)
                return 0

            return numero

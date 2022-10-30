from abc import abstractmethod, ABC

class Tela(ABC):
    @abstractmethod
    def __init__(self):
        ...

    def mostra_mensagem(self, msg):
        print('\n\%sn' % msg)

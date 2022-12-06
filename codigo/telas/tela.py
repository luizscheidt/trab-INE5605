import PySimpleGUI as sg
from abc import abstractmethod, ABC

class Tela(ABC):
    @abstractmethod
    def __init__(self):
        ...

    def mostra_mensagem(self, msg):
        sg.Popup("", msg)

    def pega_numero_conta(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('-------- SELECIONAR CONTA ----------', font=("Helvica", 25))],
            [sg.Text('Numero da conta:', size=(15, 1)), sg.InputText('', key='numero')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de livros').Layout(layout)

        button, values = self.open()

        numero = values['numero']

        if numero == '-1':
            return self.opcoes()

        try:
            numero_conta = int(numero)
        except Exception:
            self.mostra_mensagem('Número de conta inválido')
            return self.pega_numero_conta()

        return numero_conta

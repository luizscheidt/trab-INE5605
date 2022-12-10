import PySimpleGUI as sg
from .tela import Tela

class TelaSistema(Tela):
    def __init__(self, controlador):
        self.__window = None
        self.init_components()

    def opcoes(self):
        self.init_components()
        button, values = self.__window.Read()

        opcao = 0
        if button == '1':
            opcao = 1
        elif button == '2':
            opcao = 2
        elif button == '3':
            opcao = 3
        elif button == '4':
            opcao = 4
        elif button == '0':
            opcao = 0

        self.close()
        return opcao

    def close(self):
        self.__window.Close()

    def init_components(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Bem Vindo ao Sistema do Banco', justification= 'center' , size=(50,2))],
            [sg.Text('O que você deseja?', size =(25,1))],
            [sg.Button('Gerenciar Usuários', key='1')],
            [sg.Button('Gerenciar Contas', key='2')],
            [sg.Button('Gerenciar Saques e Depósitos', key='3')],
            [sg.Button(' Gerenciar Transferências', key='4')],
            [sg.Button('Encerrar', key='0')]
        ]
        self.__window = sg.Window('Sistema Bancário').Layout(layout)

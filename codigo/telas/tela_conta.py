import PySimpleGUI as sg
import re
from .tela import Tela

class TelaConta(Tela):
    def __init__(self):
        self.__window = None
        self.init_components()

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()

        return button, values

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


    def pega_cadastro_dono_conta(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('-------- DADOS CONTA ----------', font=("Helvica", 25))],
            [sg.Text('CPF/CNPJ do dono:', size=(15, 1)), sg.InputText('', key='cadastro')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de livros').Layout(layout)

        button, values = self.open()

        cadastro = values['cadastro']

        if cadastro == '-1':
            return self.opcoes()

        if not (re.match(r'^[0-9]{3}.?[0-9]{3}.?[0-9]{3}-?[0-9]{2}$', cadastro) or re.match(r'^\d{2,3}.?\d{3}.?\d{3}/?\d{4}-?\d{2}$', cadastro)):
            self.mostra_mensagem('CADASTRO INVÁLIDO')
            self.close()
        else:
            return cadastro

    def pega_saldo_conta(self):
        try:
            saldo = float(input('Saldo: '))
            if saldo < 0:
                raise ValueError
        except ValueError:
            self.mostra_mensagem('Saldo inválido')
            return self.pega_saldo_conta()

        return saldo

    def mostra_conta(self, dados_contas: list):
        for dados in dados_contas:
            print(f'-------CONTA {dados["numero"]}--------')
            print('Dono: %s' % dados['dono'])
            print('Saldo: %s' % dados['saldo'])

    def init_components(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Sistema Bancário', justification= 'center' , size=(50,2))],
            [sg.Text('CONTAS', justification='center', size =(25,1))],
            [sg.Button('Cadastra Conta', key='1')],
            [sg.Button('Excluir Conta', key='2')],
            [sg.Button('Alterar Conta', key='3')],
            [sg.Button('Lista Contas', key='4')],
            [sg.Button('Retornar', key='0')]
        ]
        self.__window = sg.Window('Sistema de livros').Layout(layout)

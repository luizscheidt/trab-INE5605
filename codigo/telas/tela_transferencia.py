import PySimpleGUI as sg
from .tela import Tela

class TelaTransferencia(Tela):
    def __init__(self, controlador_transferencias):
        self.__controlador_saque_deposito = controlador_transferencias
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Sistema Bancário', justification= 'center' , size=(50,2))],
            [sg.Text('SAQUES E DEPOSITOS', justification='center', size =(25,1))],
            [sg.Button('Realizar Transferência', key='1')],
            [sg.Button('Listar Transferência', key='2')],
            [sg.Button('Filtrar Transferências por valor', key='3')],
            [sg.Button('Filtrar Transferências por mês', key='4')],
            [sg.Button('Filtrar Transferências mais alta', key='5')],
            [sg.Button('Retornar', key='0')],
        ]

        self.__window = sg.Window('Sistema Bancário').Layout(layout)


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
        elif button == '5':
            opcao = 5
        elif button == '0':
            opcao = 0

        self.close()

        return opcao

    def pega_numero_contas(self):
        try:
            numero__origem = int(input('Número da conta que transferirá: '))
            numero__destino = int(input('Número da conta de destino: '))
        except ValueError:
            self.mostra_mensagem('Número de conta inválido')
            return self.pega_numero_contas()

        return numero__origem, numero__destino

    def pega_valor(self):
        try:
            valor = float(input('Valor: '))
            if valor < 0:
                raise ValueError
        except ValueError:
            self.mostra_mensagem('Valor inválido')
            return self.pega_valor()

        return valor

    def pega_intervalo_valores(self):
        try:
            valor_min = float(input('Valor Mínimo: '))
            valor_max = float(input('Valor Máximo: '))
        except ValueError:
            self.mostra_mensagem('Valor inválido')
            return self.pega_valor()

        if valor_min > valor_max:
            self.mostra_mensagem('Valor mínimo deve ser menor do que o máximo')
            return self.pega_intervalo_valores()

        return valor_min, valor_max

    def pega_mes(self):
        try:
            mes = int(input('Mês (0, 1, 2, ..., 11, 12): '))
            if mes not in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
                raise ValueError
        except ValueError:
            self.mostra_mensagem('Mês inválido')
            return self.pega_valor()

        return mes

    def lista_operacoes(self, operacoes):
        if operacoes:
            for op in operacoes:
                print('--------%s---------' % op['tipo'])
                print('Valor:', op['valor'])
                print('Data:', op['data'])
                print('Origem:', op['origem'])
                print('Destino:', op['destino'])
        else:
            print('Nenhuma operação registrada.')


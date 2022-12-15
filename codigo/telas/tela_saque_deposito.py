import PySimpleGUI as sg
from .tela import Tela

TITULO_FILTRAR_VALORES = '-------- FILTRAR VALORES ----------'
class TelaSaqueDeposito(Tela):

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Sistema Bancário', justification= 'center' , size=(50,2))],
            [sg.Text('SAQUES E DEPOSITOS', justification='center', size =(25,1))],
            [sg.Button('Realizar Saque', key='1')],
            [sg.Button('Realizar Deposito', key='2')],
            [sg.Button('Listar Saques', key='3')],
            [sg.Button('Listar Depositos', key='4')],
            [sg.Button('Filtrar Saques por valor', key='5')],
            [sg.Button('Filtrar Depositos por valor', key='6')],
            [sg.Button('Filtrar Saques por mês', key='7')],
            [sg.Button('Filtrar Depositos por mês', key='8')],
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
        elif button == '6':
            opcao = 6
        elif button == '7':
            opcao = 7
        elif button == '8':
            opcao = 8
        elif button == '0':
            opcao = 0

        self.close()

        return opcao

    def pega_valor(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('-------- VALOR ----------', font=("Helvica", 25))],
            [sg.Text('Valor:', size=(15, 1)), sg.InputText('', key='valor')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema Bancário').Layout(layout)

        button, values = self.open()

        if button in (None, 'Cancelar'):
            self.close()

            return 'cancelar'

        valor = values['valor']

        try:
            valor = float(valor)
            if valor < 0:
                raise ValueError
        except ValueError:
            self.mostra_mensagem('valor INVÁLIDO')
            self.close()
            return self.pega_valor()

        self.close()

        return valor

    def pega_intervalo_valores(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text(TITULO_FILTRAR_VALORES, font=("Helvica", 25))],
            [sg.Text('Valor Mínimo:', size=(15, 1)), sg.InputText('', key='min')],
            [sg.Text('Valor Máximo:', size=(15, 1)), sg.InputText('', key='max')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema Bancário').Layout(layout)

        button, values = self.open()

        if button in (None, 'Cancelar'):
            self.close()

            return 'cancelar', 'cancelar'

        try:
            valor_min = float(values['min'])
            valor_max = float(values['max'])
        except ValueError:
            self.mostra_mensagem('Valor inválido')
            self.close()

            return self.pega_intervalo_valores()

        if valor_min > valor_max:
            self.mostra_mensagem('Valor mínimo deve ser menor do que o máximo')
            self.close()

            return self.pega_intervalo_valores()

        self.close()

        return valor_min, valor_max

    def pega_mes(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text(TITULO_FILTRAR_VALORES, font=("Helvica", 25))],
            [sg.Radio('Janeiro', 'RD2', key='1')],
            [sg.Radio('Fevereiro', 'RD2', key='2')],
            [sg.Radio('Março', 'RD2', key='3')],
            [sg.Radio('Abril', 'RD2', key='4')],
            [sg.Radio('Maio', 'RD2', key='5')],
            [sg.Radio('Junho', 'RD2', key='6')],
            [sg.Radio('Julho', 'RD2', key='7')],
            [sg.Radio('Agosto', 'RD2', key='8')],
            [sg.Radio('Setembro', 'RD2', key='9')],
            [sg.Radio('Outubro', 'RD2', key='10')],
            [sg.Radio('Novembro', 'RD2', key='11')],
            [sg.Radio('Dezembro', 'RD2', key='12')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema Bancário').Layout(layout)

        button, values = self.open()

        if button in (None, 'Cancelar'):
            self.close()

            return 'cancelar'

        for valor in values:
            if values.get(valor, False):
                mes = valor

        try:
            mes = int(mes)
            if mes not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
                raise ValueError
        except ValueError:
            self.mostra_mensagem('Mês inválido')
            self.close()

            return self.pega_mes()

        self.close()

        return mes

    def lista_operacoes(self, operacoes):
        if operacoes:
            string_todas_ops = ''
            for op in operacoes:
                string_todas_ops += '--------%s---------' % op['tipo'] + '\n\n'
                string_todas_ops += 'Valor: ' + str(op['valor']) + '\n'
                string_todas_ops += 'Data: ' + op['data'] + '\n'
                string_todas_ops += 'Usuário: ' + op['dono'] + '\n'
                string_todas_ops += 'Conta: ' + str(op['conta']) + '\n'

            sg.Popup('-------- OPERAÇÕES ----------', string_todas_ops)
        else:
            self.mostra_mensagem('Nenhuma operação registrada.')

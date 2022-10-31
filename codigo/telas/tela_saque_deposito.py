from .tela import Tela

class TelaSaqueDeposito(Tela):
    def __init__(self, controlador_saque_deposito):
        self.__controlador_saque_deposito = controlador_saque_deposito

    def opcoes(self):
        print("\n--------SAQUES E TRANSFERENCIAS----------")
        print("Escolha a opcao")
        print("1 - Realizar Saque")
        print("2 - Realizar Deposito")
        print("3 - Listar Saques")
        print("4 - Listar Depositos")
        print("5 - Filtrar Saques por valor")
        print("6 - Filtrar Depositos por valor")
        print("7 - Filtrar Saques por mês")
        print("8 - Filtrar Depositos por mês")
        print("0 - Retornar\n")

        try:
            opcao = int(input('Escolha a opcao: '))
            if opcao in (0, 1, 2, 3, 4, 5, 6, 7, 8):
                return opcao
        except ValueError:
            self.mostra_mensagem('Entrada inválida.')

        return self.opcoes()

    def pega_numero_conta(self):
        try:
            numero_conta = int(input('Número da conta: '))
        except ValueError:
            self.mostra_mensagem('Número de conta inválido')
            return self.pega_numero_conta()

        return numero_conta

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
                print('Usuário:', op['dono'])
                print('Conta:', op['conta'])
        else:
            print('Nenhuma operação registrada.')

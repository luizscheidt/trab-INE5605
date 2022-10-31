from multiprocessing.sharedctypes import Value
import re
from .tela import Tela

class TelaConta(Tela):
    def __init__(self):
        ...

    def opcoes(self):
        print("\n-------- PESSOAS----------")
        print("Escolha a opcao")
        print("1 - Cadastrar Conta")
        print("2 - Excluir Conta")
        print("3 - Alterar Conta")
        print("4 - Lista Contas")
        print("0 - Retornar\n")

        try:
            opcao = int(input('Escolha a opcao: '))
            if opcao in (0, 1, 2, 3, 4, 5):
                return opcao
        except ValueError:
            self.mostra_mensagem('Entrada inválida.')

        return self.opcoes()

    def pega_cadastro_dono_conta(self):
        print('-------- DADOS CONTA----------')
        cadastro = input('CPF/CNPJ do dono: ')
        if not (re.match(r'^[0-9]{3}.?[0-9]{3}.?[0-9]{3}-?[0-9]{2}$', cadastro) or re.match(r'^\d{2,3}.?\d{3}.?\d{3}/?\d{4}-?\d{2}$', cadastro)):
            print('CADASTRO INVALIDO')
            return self.pega_cadastro_dono_conta()

        return cadastro

    def pega_numero_conta(self):
        try:
            numero_conta = int(input('Número da conta: '))
        except ValueError:
            self.mostra_mensagem('Número de conta inválido')
            return self.pega_numero_conta()

        return numero_conta

    def pega_saldo_conta(self):
        try:
            saldo = float(input('Saldo: '))
        except ValueError:
            self.mostra_mensagem('Saldo inválido')
            return self.pega_saldo_conta()

        return saldo

    def mostra_conta(self, dados_contas: list):
        for dados in dados_contas:
            print(f'-------CONTA {dados["numero"]}--------')
            print('Dono: %s' % dados['dono'])
            print('Saldo: %s' % dados['saldo'])

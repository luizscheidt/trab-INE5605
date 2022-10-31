from .tela import Tela

class TelaSistema(Tela):
    def __init__(self, controlador):
        self.__controlador = controlador

    def opcoes(self):
        print("\n-------- SISTEMA ----------")
        print("Escolha a opcao")
        print("1 - Gerenciar Usuários")
        print("2 - Gerenciar Contas")
        print("3 - Gerenciar Saques e Depósitos")
        print("4 - Gerenciar Transferências")
        print("0 - Encerrar\n")

        try:
            opcao = int(input('Escolha a opcao: '))
            if opcao in (0, 1, 2, 3, 4):
                return opcao
        except ValueError:
            self.mostra_mensagem('Entrada inválida.')

        return self.opcoes()

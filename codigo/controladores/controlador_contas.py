from telas.tela_conta import TelaConta
from modelos.conta_corrente import ContaCorrente

class ControladorConta:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_contas = TelaConta()
        self.__contas_por_numero = {} # numero: conta
        self.__contas_por_dono = {} # dono: conta

    def pega_conta_por_numero(self, numero: float):
        if conta := self.__contas_por_numero.get(numero):
            return conta

        raise ContaInexistenteException

    def pega_conta_por_dono(self, dono):
        if conta := self.__contas_por_dono.get(dono):
            return conta

        raise ContaInexistenteException

    def cadastrar_conta(self):
        dados_conta = self.__tela_contas.pega_dados_conta()
        try:
            conta = ContaCorrente(**dados_conta)
            self.__contas_por_numero[conta.numero] = conta
            self.__contas_por_dono[conta.dono] = conta
        except ContaJaCadastradaException:
            self.__tela_contas.mostra_mensagem('ATENÇÃO: Conta já cadastrada')
        else:
            self.__tela_contas.mostra_mensagem('Conta cadastrada com sucesso.')

    def alterar_conta(self, conta):
        self.lista_contas()
        identificador_conta = self.__tela_pessoas.seleciona_conta()

        try:
            if self.__contas_por_dono.get(identificador_conta):
                conta = self.__contas_por_dono[identificador_conta]
            elif self.__contas_por_numero.get(identificador_conta):
                conta = self.__contas_por_dono[identificador_conta]
        except ContaInexistenteException:
            self.__tela_contas.mostra_mensagem('ATENÇÃO: Conta inexistente.')

        novos_dados = self.__tela_contas.pega_dados_conta()
        for atributo, valor in novos_dados:
            setattr(conta, atributo, valor)
        self.__tela_pessoas.mostra_mensagem('Dados da conta alterados com sucesso.')

    def lista_contas(self):
        dados_contas = [{
            'dono': conta.dono,
            'saldo': conta.saldo,
            'numero': conta.numero,
            'transferencias': conta.transferencias,
            } for numero, conta in self.__contas_por_numero
        ]

        self.__tela_contas.mostra_conta(dados_contas)

    def excluir_conta(self):
        self.lista_contas()
        identificador_conta = self.__tela_pessoas.seleciona_pessoa()

        try:
            if self.__contas_por_dono.get(identificador_conta):
                conta = self.__contas_por_dono[identificador_conta]
            elif self.__contas_por_numero.get(identificador_conta):
                conta = self.__contas_por_dono[identificador_conta]
        except ContaInexistenteException:
            self.__tela_contas.mostra_mensagem('ATENÇÃO: Conta inexistente.')

        self.__contas_por_dono.pop(conta.dono)
        self.__contas_por_numero.pop(conta.numero)

        self.__tela_contas.mostra_mensagem('Conta excluída com sucesso.')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.cadastrar_conta,
            2: self.alterar_conta,
            3: self.excluir_conta,
            4: self.lista_contas,
            0: self.retornar,
        }

        while True:
            funcao_escolhida = opcoes[self.__tela_contas.tela_opcoes()]
            funcao_escolhida()


class ContaInexistenteException(BaseException):
    ...


class ContaJaCadastradaException(BaseException):
    ...

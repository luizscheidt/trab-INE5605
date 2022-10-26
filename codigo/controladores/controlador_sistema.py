from telas.tela_sistema import TelaSistema
from controlador_contas import ControladorConta
from controlador_pessoa import ControladorPessoa
from controlador_saque_deposito import ControladorSaqueDeposito
from controlador_transferencia import ControladorTransferencia


class ControladorSistema:

    def __init__(self):
        self.__tela = TelaSistema(self)
        self.__controlador_contas = ControladorConta(self)
        self.__controlador_pessoa = ControladorPessoa(self)
        self.__controlador_saque_deposito = ControladorSaqueDeposito(self)
        self.__controlador_transferencia = ControladorTransferencia(self)

    @property
    def tela(self):
        return self.__tela

    @property
    def controlador_conta(self):
        return self.__controlador_contas

    @property
    def controlador_pessoa(self):
        return self.__controlador_pessoa

    @property
    def controlador_saque_deposito(self):
        return self.__controlador_saque_deposito

    @property
    def controlador_transferencia(self):
        return self.__controlador_transferencia

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_pessoa(self):
        self.controlador_pessoa.abre_tela()

    def cadastra_conta(self):
        self.controlador_conta.abre_tela()

    def realiza_saque_deposito(self):
        self.controlador_saque_deposito.abre_tela()

    def realiza_transferencia(self):
        self.controlador_transferencia.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.cadastra_pessoa,
            2: self.cadastra_conta,
            3: self.realiza_saque_deposito,
            4: self.realiza_transferencia,
        }

        while True:
            opcao_escolhida = self.__tela.opcoes()
            funcao_escolhida = opcoes.get(opcao_escolhida)
            funcao_escolhida()

    def encerra_sistema(self):
        exit(0)

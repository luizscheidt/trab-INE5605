from telas.tela_conta import TelaConta
from modelos.conta_corrente import ContaCorrente
from controladores.controlador_pessoa import PessoaInexistenteException
from DAOs.conta_dao import ContaDAO
from DAOs.numeros_dao import NumeroDAO


class ControladorConta:
    def __init__(self, controlador_sistema, controlador_pessoas):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_pessoas = controlador_pessoas
        self.__tela_contas = TelaConta()
        self.__gerador_numero = NumeroConta()
        self.__dao = ContaDAO()

    @property
    def DAO(self):
        return self.__dao

    @property
    def contas(self):
        return self.DAO.get_all()

    @property
    def contas_por_dono(self):
        contas_por_dono = {}
        for conta in self.contas:
            contas_por_dono[conta.dono] = conta

    def atualiza_conta(self, conta):
        self.DAO.update(conta.numero, conta)

    def pega_conta_por_numero(self, numero: float):
        if conta := self.DAO.get(numero):
            return conta

        raise ContaInexistenteException

    def pega_conta_por_dono(self, dono):
        if conta := self.contas_por_dono.get(dono):
            return conta

        raise ContaInexistenteException

    def cadastrar_conta(self):
        cadastro_dono, saldo = self.__tela_contas.pega_cadastro_dono_conta()

        if cadastro_dono == 'cancelar':
            return self.abre_tela()

        try:
            dono = self.__controlador_pessoas.pega_pessoa_por_cadastro(cadastro_dono)
            if dono.conta:
                self.__tela_contas.mostra_mensagem('ATENÇÃO: Este usuário já possui conta.')
                return self.abre_tela()
        except PessoaInexistenteException:
            self.__tela_contas.mostra_mensagem('ATENÇÃO: Usuário inexistente.')
            return self.cadastrar_conta()

        numero = self.__gerador_numero.gera_numero()
        conta = ContaCorrente(dono=dono, numero=numero, saldo=saldo)
        self.DAO.add(conta)
        dono.conta = conta
        self.__controlador_pessoas.atualiza_pessoa(dono)

        self.__tela_contas.mostra_mensagem('Conta cadastrada com sucesso.')

    def alterar_conta(self):
        identificador_conta = self.__tela_contas.pega_numero_conta()

        if identificador_conta == 'cancelar':
            return self.abre_tela()

        try:
            conta = self.pega_conta_por_numero(identificador_conta)
        except ContaInexistenteException:
            self.__tela_contas.mostra_mensagem('ATENÇÃO: Conta inexistente.')
            return self.alterar_conta()

        cadastro_dono = self.__tela_contas.pega_cadastro_dono_conta()
        try:
            dono = self.__controlador_pessoas.pega_pessoa_por_cadastro(cadastro_dono)
        except PessoaInexistenteException:
            self.__tela_contas.mostra_mensagem('ATENÇÃO: Usuário inexistente.')
            return self.alterar_conta()

        saldo = self.__tela_contas.pega_saldo_conta()

        novos_dados = {
            'dono': dono,
            'saldo': saldo,
        }

        for atributo, valor in novos_dados.items():
            setattr(conta, atributo, valor)

        self.DAO.update(conta.numero, conta)

        self.__tela_contas.mostra_mensagem('Dados da conta alterados com sucesso.')

    def lista_contas(self):
        dados_contas = [{
            'dono': conta.dono.representacao,
            'saldo': conta.saldo,
            'numero': conta.numero,
            } for conta in self.contas
        ]

        return self.__tela_contas.mostra_conta(dados_contas)

    def excluir_conta(self):
        identificador_conta = self.__tela_contas.pega_numero_conta()

        if identificador_conta == 'cancelar':
            return self.abre_tela()

        try:
            conta = self.pega_conta_por_numero(identificador_conta)
        except ContaInexistenteException:
            self.__tela_contas.mostra_mensagem('ATENÇÃO: Conta inexistente.')
            return self.excluir_conta()

        self.DAO.remove(conta.numero)
        conta.dono.conta = None
        self.__controlador_pessoas.atualiza_pessoa(conta.dono)

        self.__tela_contas.mostra_mensagem('Conta excluída com sucesso.')

    def retornar(self):
        return self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.cadastrar_conta,
            2: self.excluir_conta,
            3: self.alterar_conta,
            4: self.lista_contas,
            0: self.retornar,
        }

        while True:
            funcao_escolhida = opcoes[self.__tela_contas.opcoes()]
            funcao_escolhida()


class NumeroConta:
    def __init__(self):
        self.__dao = NumeroDAO()

    @property
    def ultimo_numero(self):
        numero = self.__dao.get('conta')
        return numero

    def gera_numero(self):
        numero = self.ultimo_numero + 1
        self.__dao.add('conta', numero)
        return numero


class ContaInexistenteException(BaseException):
    ...

class MesmaContaException(BaseException):
    ...


class ContaJaCadastradaException(BaseException):
    ...

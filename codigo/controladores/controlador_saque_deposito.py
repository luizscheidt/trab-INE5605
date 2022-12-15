from controladores.controlador_contas import ContaInexistenteException
from modelos.deposito import Deposito
from modelos.saque import Saque
from modelos.data import Data
from telas.tela_saque_deposito import TelaSaqueDeposito
from telas.tela_conta import TelaConta
from DAOs.saque_deposito_dao import SaqueDepositoDAO
from DAOs.numeros_dao import NumeroDAO

class ControladorSaqueDeposito:
    def __init__(self, controlador_sistema, controlador_contas):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_contas = controlador_contas
        self.__tela = TelaSaqueDeposito()
        self.__dao = SaqueDepositoDAO()
        self.__gerador_numero = NumeroOperacao()

    @property
    def DAO(self):
        return self.__dao

    @property
    def operacoes(self):
        return self.DAO.get_all()

    @property
    def saques(self):
        saques = []
        for op in self.operacoes:
            if op.tipo == 'saque':
                saques.append(op)

        return saques

    @property
    def depositos(self):
        depositos = []
        for op in self.operacoes:
            if op.tipo == 'deposito':
                depositos.append(op)

        return depositos

    def realizar_operacao(self, tipo):
        identificador_conta = TelaConta().pega_numero_conta()

        if identificador_conta == 'cancelar':
            return self.abre_tela()

        try:
            conta = self.__controlador_contas.pega_conta_por_numero(identificador_conta)
            self.__tela.mostra_mensagem('Saldo Disponível: %s' % conta.saldo)
        except ContaInexistenteException:
            self.__tela.mostra_mensagem('ATENÇÃO: Conta inexistente')
            return self.abre_tela()

        valor = self.__tela.pega_valor()

        if tipo == 'saque':
            if valor < conta.saldo:
                conta.saldo -= valor
                id = self.__gerador_numero.gera_numero()
                saque = Saque(id, valor=valor, conta=conta, data=Data.hoje())
                self.DAO.add(saque)
            else:
                self.__tela.mostra_mensagem('SALDO INSUFICIENTE')
                return self.abre_tela()
        elif tipo == 'deposito':
            conta.saldo += valor
            id = self.__gerador_numero.gera_numero()
            deposito = Deposito(id, valor=valor, conta=conta, data=Data.hoje())
            self.DAO.add(deposito)

        self.__controlador_contas.atualiza_conta(conta)
        self.__tela.mostra_mensagem('Operação realizada com sucesso')

    def realizar_saque(self):
        return self.realizar_operacao(tipo='saque')

    def realizar_deposito(self):
        return self.realizar_operacao(tipo='deposito')

    def mostra_operacoes(self, operacoes):
        dados = []
        for operacao in operacoes:
            dados.append({
                'valor': operacao.valor,
                'data': operacao.data,
                'conta': operacao.conta.numero,
                'dono': operacao.conta.dono.representacao,
                'tipo': operacao.tipo,
            })

        return self.__tela.lista_operacoes(dados)


    def listar_operacoes(self, tipo):
        operacoes = []
        if tipo == 'saque':
            operacoes = self.saques
        elif tipo == 'deposito':
            operacoes = self.depositos

        return self.mostra_operacoes(operacoes)

    def listar_saques(self):
        self.listar_operacoes('saque')

    def listar_depositos(self):
        self.listar_operacoes('deposito')

    def filtar_operacoes_por_valor(self, tipo):
        operacoes_filtradas = []
        valor_min, valor_max = self.__tela.pega_intervalo_valores()

        if valor_min == 'cancelar':
            return self.abre_tela()

        if tipo == 'saque':
            operacoes = self.saques
        elif tipo == 'deposito':
            operacoes = self.depositos

        for op in operacoes:
            if valor_min < op.valor and valor_max > op.valor:
                operacoes_filtradas.append(op)

        return self.mostra_operacoes(operacoes_filtradas)

    def filtrar_saques_por_valor(self):
        return self.filtar_operacoes_por_valor(tipo='saque')

    def filtrar_depositos_por_valor(self):
        return self.filtar_operacoes_por_valor(tipo='deposito')

    def filtrar_operacoes_por_mes(self, tipo):
        mes = self.__tela.pega_mes()
        mes = f'/{mes:02}/'
        operacoes_filtradas = []

        if tipo == 'saque':
            operacoes = self.saques
        elif tipo == 'deposito':
            operacoes = self.depositos

        for op in operacoes:
            if mes in op.data:
                operacoes_filtradas.append(op)

        return self.mostra_operacoes(operacoes_filtradas)

    def filtrar_saques_por_mes(self):
        return self.filtrar_operacoes_por_mes(tipo='saque')

    def filtrar_depositos_por_mes(self):
        return self.filtrar_operacoes_por_mes(tipo='deposito')

    def retornar(self):
        return self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.realizar_saque,
            2: self.realizar_deposito,
            3: self.listar_saques,
            4: self.listar_depositos,
            5: self.filtrar_saques_por_valor,
            6: self.filtrar_depositos_por_valor,
            7: self.filtrar_saques_por_mes,
            8: self.filtrar_depositos_por_mes,
            0: self.retornar,
        }

        while True:
            funcao_escolhida = opcoes[self.__tela.opcoes()]
            funcao_escolhida()

class NumeroOperacao:
    def __init__(self):
        self.__dao = NumeroDAO()

    @property
    def ultimo_numero(self):
        numero = self.__dao.get('operacao')
        return numero

    def gera_numero(self):
        numero = self.ultimo_numero + 1
        self.__dao.add('operacao', numero)
        return numero

from modelos.transferencia import Transferencia
from modelos.data import Data
from controladores.controlador_contas import ContaInexistenteException, MesmaContaException
from telas.tela_transferencia import TelaTransferencia
from DAOs.transferencia_dao import TransferenciaDAO
from DAOs.numeros_dao import NumeroDAO


class ControladorTransferencia:
    def __init__(self, controlador_sistema, controlador_contas):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_contas = controlador_contas
        self.__tela = TelaTransferencia()
        self.__gerador_numero = NumeroTransferencia()
        self.__DAO = TransferenciaDAO()

    @property
    def DAO(self):
        return self.__DAO

    @property
    def transferencias(self):
        return self.DAO.get_all()

    def realizar_transferencia(self):
        self.__controlador_contas.lista_contas()
        id_origem, id_destino = self.__tela.pega_numero_contas()

        if id_origem == 'cancelar':
            return self.abre_tela()

        try:
            origem = self.__controlador_contas.pega_conta_por_numero(id_origem)
            destino = self.__controlador_contas.pega_conta_por_numero(id_destino)
            if origem == destino:
                raise MesmaContaException
            self.__tela.mostra_mensagem('Saldo Disponível: %s' % origem.saldo)
        except ContaInexistenteException:
            self.__tela.mostra_mensagem('ATENÇÃO: Conta inexistente')
            return self.abre_tela()
        except MesmaContaException:
            self.__tela.mostra_mensagem('ATENÇÃO: A transferência deve ser feita entre contas diferentes')
            return self.abre_tela()

        valor = self.__tela.pega_valor()
        if valor == 'cancelar':
            return self.abre_tela()

        if valor < origem.saldo:
            origem.saldo -= valor
            destino.saldo += valor
            id = self.__gerador_numero.gera_numero()
            transferencia = Transferencia(id, origem, destino, valor, data=Data.hoje())
            self.DAO.add(transferencia)
        else:
            self.__tela.mostra_mensagem('SALDO INSUFICIENTE')
            return self.abre_tela()

        self.__controlador_contas.atualiza_conta(origem)
        self.__controlador_contas.atualiza_conta(destino)
        self.__tela.mostra_mensagem('Operação realizada com sucesso')

    def mostra_operacoes(self, operacoes):
        dados = []
        for operacao in operacoes:
            if operacao:
                dados.append({
                    'valor': operacao.valor,
                    'data': operacao.data,
                    'origem': operacao.origem.numero,
                    'destino': operacao.destino.numero,
                    'tipo': 'Transferência',
               })

        return self.__tela.lista_operacoes(dados)


    def listar_transferencias(self):
        return self.mostra_operacoes(self.transferencias)

    def filtar_transferencias_por_valor(self):
        operacoes_filtradas = []
        valor_min, valor_max = self.__tela.pega_intervalo_valores()
        if valor_min == 'cancelar':
            return self.abre_tela()

        for op in self.transferencias:
            if valor_min < op.valor and valor_max > op.valor:
                operacoes_filtradas.append(op)

        return self.mostra_operacoes(operacoes_filtradas)

    def filtrar_transferencias_por_mes(self):
        mes = self.__tela.pega_mes()
        if mes == 'cancelar':
            return self.abre_tela()

        mes = f'/{mes:02}/'
        operacoes_filtradas = []

        for op in self.transferencias:
            if mes in op.data:
                operacoes_filtradas.append(op)

        return self.mostra_operacoes(operacoes_filtradas)

    def filtrar_transferencia_mais_alta(self):
        max = 0
        mais_alta = None

        for op in self.transferencias:
            if op.valor > max:
                mais_alta = op
                max = op.valor

        return self.mostra_operacoes([mais_alta])

    def retornar(self):
        return self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.realizar_transferencia,
            2: self.listar_transferencias,
            3: self.filtar_transferencias_por_valor,
            4: self.filtrar_transferencias_por_mes,
            5: self.filtrar_transferencia_mais_alta,
            0: self.retornar,
        }

        while True:
            funcao_escolhida = opcoes[self.__tela.opcoes()]
            funcao_escolhida()


class NumeroTransferencia:
    def __init__(self):
        self.__dao = NumeroDAO()

    @property
    def ultimo_numero(self):
        numero = self.__dao.get('transferencia')
        return numero

    def gera_numero(self):
        numero = self.ultimo_numero + 1
        self.__dao.add('transferencia', numero)
        return numero

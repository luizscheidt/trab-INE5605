from telas.tela_pessoa import TelaPessoa
from modelos.cpf import Cpf
from modelos.cnpj import Cnpj
from modelos.pessoa_fisica import PessoaFisica
from modelos.pessoa_juridica import PessoaJuridica

class ControladorPessoa:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_pessoas = TelaPessoa()
        self.__pessoas_juridicas = {}
        self.__pessoas_fisicas = {}
        self.__pessoas_por_tipo = {
            'fisica': self.__pessoas_fisicas,
            'juridica': self.__pessoas_juridicas,
        }

    @property
    def pessoas_fisicas(self):
        return self.__pessoas_fisicas

    @property
    def pessoas_juridicas(self):
        return self.__pessoas_juridicas

    def pega_pessoa_por_cadastro(self, cadastro):
        if isinstance(cadastro, Cpf):
            return self.__pessoas_fisicas.get(cadastro)
        elif isinstance(cadastro, Cnpj):
            return self.__pessoas_juridicas.get(cadastro)

        raise PessoaInexistenteException

    def pega_pessoa_por_cnpj(self, cnpj: Cnpj):
        return self.__pessoas_juridicas.get(cnpj)

    def cadastrar_pessoa(self, tipo_pessoa):
        dados_pessoa = self.__tela_pessoas.pega_dados_pessoa(tipo_pessoa)
        try:
            if tipo_pessoa == 'fisica':
                pessoa = PessoaFisica(**dados_pessoa)
                self.__pessoas_juridicas[pessoa.cpf] = pessoa
            elif tipo_pessoa == 'juridica':
                pessoa = PessoaJuridica(**dados_pessoa)
                self.__pessoas_fisicas[pessoa.cnpj] = pessoa
        except PessoaJaCadastradaException:
            self.__tela_pessoas.mostra_mensagem('ATENÇÃO: Pessoa já cadastrada')
        else:
            self.__tela_pessoas.mostra_mensagem('Pessoa cadastrada com sucesso.')

    def cadastrar_pessoa_fisica(self):
        self.cadastrar_pessoa(tipo_pessoa='fisica')

    def cadastrar_pessoa_juridica(self):
        self.cadastrar_pessoa(tipo_pessoa='juridica')

    def alterar_pessoa(self, tipo_pessoa):
        self.lista_pessoa(tipo_pessoa)
        cadastro_pessoa = self.__tela_pessoas.seleciona_pessoa()

        try:
            if cpf := Cpf.valida(cadastro_pessoa):
                pessoa = self.pega_pessoa_por_cadastro(cpf)
            elif cnpj := Cnpj.valida(cadastro_pessoa):
                pessoa = self.pega_pessoa_por_cadastro(cnpj)
        except PessoaInexistenteException:
            self.__tela_pessoas.mostra_mensagem('ATENÇÃO: Pessoa inexistente.')

        novos_dados = self.__tela_pessoas.pega_dados_pessoa()
        for atributo, valor in novos_dados:
            setattr(pessoa, atributo, valor)
        self.__tela_pessoas.mostra_mensagem('Dados pessoais alterados com sucesso.')

    def lista_pessoas(self, tipo_pessoa):
        pessoas = self.__pessoas_por_tipo.get(tipo_pessoa)
        if tipo_pessoa == 'fisica':
            dados_pessoas = [{
                'nome': pessoa.nome,
                'cpf': pessoa.cpf,
            }
                for pessoa in pessoas
            ]
        elif tipo_pessoa == 'juridica':
            dados_pessoas = [
                {
                'nome': pessoa.nome,
                'cnpj': pessoa.cnpj,
            }
                for pessoa in pessoas
            ]

        self.__tela_pessoas.mostra_pessoa(dados_pessoas)

    def excluir_pessoa(self, tipo_pessoa):
        self.lista_pessoas(tipo_pessoa)
        cadastro_pessoa = self.__tela_pessoas.seleciona_pessoa()
        pessoa_excluida = False

        try:
            if cpf := Cpf.valida(cadastro_pessoa):
                pessoa = self.pega_pessoa_por_cadastro(cpf)
                self.__pessoas_fisicas.pop(cpf, None)
            elif cnpj := Cnpj.valida(cadastro_pessoa):
                pessoa = self.pega_pessoa_por_cadastro(cnpj)
                self.__pessoas_juridicas.pop(cnpj, None)

            mensagem = f'Pessoa excluida com sucesso. {pessoa.nome}, {pessoa.cadastro}'
        except PessoaInexistenteException:
            mensagem = 'ATENÇÃO: Pessoa inexistente'

        self.__tela_pessoas.mostra_mensagem(mensagem)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.cadastrar_pessoa_fisica,
            2: self.cadastrar_pessoa_juridica,
            3: self.alterar_pessoa,
            4: self.lista_pessoas,
            5: self.excluir_pessoa,
            0: self.retornar,
        }

        while True:
            funcao_escolhida = opcoes[self.__tela_pessoa.tela_opcoes()]
            funcao_escolhida()


class PessoaInexistenteException(BaseException):
    ...


class PessoaJaCadastradaException(BaseException):
    ...

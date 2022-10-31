from telas.tela_pessoa import TelaPessoa
from modelos.cpf import Cpf, CpfInvalidoException
from modelos.cnpj import Cnpj, CnpjInvalidoException
from modelos.pessoa_fisica import PessoaFisica
from modelos.pessoa_juridica import PessoaJuridica

class ControladorPessoa:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_pessoas = TelaPessoa()
        self.__pessoas_juridicas = {}
        self.__pessoas_fisicas = {}

    @property
    def pessoas_fisicas(self):
        return self.__pessoas_fisicas

    @property
    def pessoas_juridicas(self):
        return self.__pessoas_juridicas

    @property
    def pessoas_por_cadastro(self):
        pessoas_por_cadastro = {}

        for cadastro, pessoa in self.__pessoas_fisicas.items():
            pessoas_por_cadastro[cadastro] = pessoa
        for cadastro, pessoa in self.__pessoas_juridicas.items():
            pessoas_por_cadastro[cadastro] = pessoa

        return pessoas_por_cadastro

    def pessoas_por_tipo(self, tipo):
        if tipo == 'fisica':
            return self.__pessoas_fisicas
        elif tipo == 'juridica':
            return self.__pessoas_juridicas

    def pega_pessoa_por_cadastro(self, cadastro):
        cadastro = cadastro.replace('.', '').replace('-', '').replace('/', '')
        pessoas = list(self.__pessoas_fisicas.values()) + list(self.__pessoas_juridicas.values())
        for pessoa in pessoas:
            if pessoa.cadastro == cadastro:
                return pessoa

        raise PessoaInexistenteException

    def cadastrar_pessoa(self, tipo_pessoa):
        dados_pessoa = self.__tela_pessoas.pega_dados_pessoa(tipo_pessoa)

        if tipo_pessoa == 'fisica':
            if dados_pessoa['cpf'] not in self.__pessoas_fisicas:
                try:
                    pessoa = PessoaFisica(**dados_pessoa)
                    self.__pessoas_fisicas[pessoa.cpf] = pessoa
                except CpfInvalidoException:
                    self.__tela_pessoas.mostra_mensagem('ATENÇÃO: CPF inválido.')
                    return self.cadastrar_pessoa(tipo_pessoa)
            else:
                self.__tela_pessoas.mostra_mensagem('ATENÇÃO: Pessoa já cadastrada')
                return self.cadastrar_pessoa(tipo_pessoa)
        elif tipo_pessoa == 'juridica':
            if dados_pessoa['cnpj'] not in self.__pessoas_juridicas:
                try:
                    pessoa = PessoaJuridica(**dados_pessoa)
                    self.__pessoas_juridicas[pessoa.cnpj] = pessoa
                except CnpjInvalidoException:
                    self.__tela_pessoas.mostra_mensagem('ATENÇÃO: CNPJ inválido.')
                    return self.cadastrar_pessoa(tipo_pessoa)
            else:
                self.__tela_pessoas.mostra_mensagem('ATENÇÃO: Pessoa já cadastrada')
                return self.cadastrar_pessoa(tipo_pessoa)

        self.__tela_pessoas.mostra_mensagem('Pessoa cadastrada com sucesso.')

    def cadastrar_pessoa_fisica(self):
        self.cadastrar_pessoa(tipo_pessoa='fisica')

    def cadastrar_pessoa_juridica(self):
        self.cadastrar_pessoa(tipo_pessoa='juridica')

    def alterar_pessoa(self):
        cadastro_pessoa = self.__tela_pessoas.pega_cadastro()

        try:
            pessoa = self.pega_pessoa_por_cadastro(cadastro_pessoa)
            self.lista_pessoa(pessoa)
        except PessoaInexistenteException:
            self.__tela_pessoas.mostra_mensagem('ATENÇÃO: Pessoa inexistente.')
            self.alterar_pessoa()

        novos_dados = self.__tela_pessoas.pega_dados_pessoa(pessoa.tipo)

        for atributo, valor in novos_dados.items():
            setattr(pessoa, atributo, valor)

        self.__tela_pessoas.mostra_mensagem('Dados pessoais alterados com sucesso.')

    def lista_pessoa(self, pessoa):
        if pessoa.tipo == 'fisica':
            dados_pessoa = {
                'nome': pessoa.nome,
                'cpf': pessoa.cpf,
            }
        elif pessoa.tipo == 'juridica':
            dados_pessoa = {
                'razao_social': pessoa.razao_social,
                'cnpj': pessoa.cnpj,
            }

        self.__tela_pessoas.mostra_pessoa([dados_pessoa])


    def lista_pessoas(self, tipo_pessoa):
        pessoas = self.pessoas_por_tipo(tipo_pessoa)

        if tipo_pessoa == 'fisica':
            dados_pessoas = [{
                'nome': pessoa.nome,
                'cpf': pessoa.cpf,
            }
                for pessoa in pessoas.values()
            ]
        elif tipo_pessoa == 'juridica':
            dados_pessoas = [
                {
                'razao_social': pessoa.razao_social,
                'cnpj': pessoa.cnpj,
            }
                for pessoa in pessoas.values()
            ]

        self.__tela_pessoas.mostra_pessoa(dados_pessoas)

    def lista_pessoas_fisicas(self):
        self.lista_pessoas('fisica')

    def lista_pessoas_juridicas(self):
        self.lista_pessoas('juridica')

    def excluir_pessoa(self):
        cadastro_pessoa = self.__tela_pessoas.pega_cadastro()

        try:
            pessoa = self.pega_pessoa_por_cadastro(cadastro_pessoa)
            if pessoa.tipo == 'fisica':
                self.__pessoas_fisicas.pop(pessoa.cpf, None)
            elif pessoa.tipo == 'juridica':
                self.__pessoas_juridicas.pop(pessoa.cnpj, None)
            self.__tela_pessoas.mostra_mensagem(f'Pessoa excluida com sucesso. {pessoa.nome}, {pessoa.cadastro}')
        except PessoaInexistenteException:
            self.__tela_pessoas.mostra_mensagem('ATENÇÃO: Pessoa inexistente.')
            self.excluir_pessoa()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.cadastrar_pessoa_fisica,
            2: self.cadastrar_pessoa_juridica,
            3: self.alterar_pessoa,
            4: self.lista_pessoas_fisicas,
            5: self.lista_pessoas_juridicas,
            6: self.excluir_pessoa,
            0: self.retornar,
        }

        while True:
            funcao_escolhida = opcoes[self.__tela_pessoas.opcoes()]
            funcao_escolhida()


class PessoaInexistenteException(BaseException):
    ...


class PessoaJaCadastradaException(BaseException):
    ...

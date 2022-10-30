from controladores.controlador_pessoa import ControladorPessoa, PessoaJaCadastradaException
from pessoa import Pessoa
from cpf import Cpf


class PessoaFisica(Pessoa):
    def __init__(self, email: str, fone: str, cpf: Cpf,  nome: str):
        super().__init__(email, fone)
        if isinstance(cpf, Cpf):
            self.__cpf = cpf
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def cpf(self):
        return '%s' % self.__cpf

    @cpf.setter
    def cpf(self, cpf: Cpf):
        if cpf in ControladorPessoa.pessoas_fisicas:
            raise PessoaJaCadastradaException

        if isinstance(cpf, Cpf):
            self.__cpf = cpf

    @property
    def cadastro(self):
        return '%s' % self.__cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

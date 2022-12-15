from DAOs.dao import DAO
from modelos.pessoa import Pessoa
from modelos.pessoa_fisica import PessoaFisica
from modelos.pessoa_juridica import PessoaJuridica

class PessoaDAO(DAO):
    def __init__(self):
        super().__init__('pessoas.pkl')

    def add(self, pessoa: Pessoa):
        if pessoa and isinstance(pessoa, (PessoaFisica, PessoaJuridica)) and isinstance(pessoa.cadastro, str):
            if self.get(pessoa.cadastro):
                raise PessoaJaCadastradaException

            super().add(pessoa.cadastro, pessoa)

    def get(self, cadastro: str):
        if isinstance(cadastro, str):
            return super().get(cadastro)

    def remove(self, cadastro: str):
        if isinstance(cadastro, str):
            return super().remove(cadastro)


class PessoaJaCadastradaException(BaseException):
    ...

from .cnpj import Cnpj
from .pessoa import Pessoa


class PessoaJuridica(Pessoa):
    def __init__(self, email: str, fone: str, cnpj: str,  razao_social: str):
        super().__init__(email, fone)
        self.__cnpj = Cnpj(cnpj)
        self.__razao_social = razao_social


    @property
    def cnpj(self):
        return '%s' % self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj: str):
        if isinstance(cnpj, str):
            self.__cnpj = cnpj

    @property
    def cadastro(self):
        return '%s' % self.__cnpj

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def tipo(self):
        return 'juridica'

    @razao_social.setter
    def razao_social(self, razao_social: str):
        if isinstance(razao_social, str):
            self.__razao_social = razao_social

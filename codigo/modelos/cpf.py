class Cpf:
    def __init__(self, cpf: str):
        if cpf := self.valida(cpf):
            self.__cpf = cpf
        else:
            raise CpfInvalidoException

    def valida(self, cpf: str):
        cpf = cpf.replace('.', '')
        cpf = cpf.replace('-', '')

        def eh_sequencia(cpf):
            if cpf[0] * len(cpf) == cpf:
                return True
            else:
                return False

        if not cpf or len(cpf) != 11 or eh_sequencia(cpf):
            return False

        cpf1 = cpf[0:9]

        soma = 0
        contagem = 10
        for i in range(9):
            soma += int(cpf1[i]) * contagem
            contagem -= 1
        if 11 - (soma % 11) > 9:
            cpf1 += '0'
        else:
            cpf1 += str(11 - soma % 11)

        soma = 0
        contagem = 11
        for i in range(10):
            soma += int(cpf1[i]) * contagem
            contagem -= 1
        if 11 - (soma % 11) > 9:
            cpf1 += '0'
        else:
            cpf1 += str(11 - soma % 11)

        if cpf == cpf1:
            return cpf

    @property
    def com_pontuacao(self):
        if not hasattr(self, '__com_pontuacao'):
            cpf_com_pontuacao = self.__cpf[:3] + '.' + self.__cpf[3:6] + '.' + self.__cpf[6:9] + '-' + self.__cpf[9:]
            self.__com_pontuacao = cpf_com_pontuacao

        return self.__com_pontuacao

    def __repr__(self):
        return self.__cpf


class CpfInvalidoException(BaseException):
    ...

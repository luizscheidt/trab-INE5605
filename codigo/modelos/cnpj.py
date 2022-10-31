class Cnpj:
    def __init__(self, cnpj):
        if cnpj := self.valida(cnpj):
            self.__cnpj = cnpj
        else:
            raise CnpjInvalidoException

    def valida(self, cnpj: str):
        k1 = '543298765432'
        k1 = list(k1)

        def remove_carac(string: str):
            string = string.replace('.', '')
            string = string.replace('/', '')
            string = string.replace('-', '')
            return string

        cnpj_original = remove_carac(cnpj)
        novo_cnpj = remove_carac(cnpj)

        def eh_sequencia(f):
            if f[0] * len(f) == f:
                return True
            else:
                return False

        if eh_sequencia(novo_cnpj):
            return False

        novo_cnpj = novo_cnpj[0:12]
        temp = list(novo_cnpj)
        for i in range(12):
            temp[i] = int(temp[i])
            k1[i] = int(k1[i])
            temp[i] *= k1[i]

        soma = 0
        for j in temp:
            soma += int(j)

        if 11 - (soma % 11) <= 9:
            novo_cnpj += str(11 - (soma % 11))
        else:
            novo_cnpj += '0'

        k2 = '6543298765432'
        k2 = list(k2)

        temp = list(novo_cnpj)
        for i in range(13):
            temp[i] = int(temp[i])
            k2[i] = int(k2[i])
            temp[i] *= k2[i]

        soma = 0
        for j in temp:
            soma += int(j)

        if 11 - (soma % 11) <= 9:
            novo_cnpj += str(11 - (soma % 11))
        else:
            novo_cnpj += '0'

        if cnpj_original == novo_cnpj:
            return novo_cnpj

    @property
    def com_pontuacao(self):
        if not hasattr(self, '__com_pontuacao'):
            cnpj_com_pontuacao = self.__cnpj[:2] + '.' + self.__cnpj[2:5] + '.' + self.__cnpj[5:8] + '/' + self.__cnpj[8:12] + '-' + self.__cnpj[12:]
            self.__com_pontuacao = cnpj_com_pontuacao

        return self.__com_pontuacao

    def __repr__(self):
        return self.__cnpj

class CnpjInvalidoException(BaseException):
    ...

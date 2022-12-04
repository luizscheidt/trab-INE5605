import re
from .tela import Tela

class TelaPessoa(Tela):
    def __init__(self):
        ...

    def opcoes(self):
        print("\n-------- PESSOAS----------")
        print("Escolha a opcao")
        print("1 - Cadastrar Pessoa Fisica")
        print("2 - Cadastrar Pessoa Juridica")
        print("3 - Alterar Usuário")
        print("4 - Listar Pessoas Físicas")
        print("5 - Listar Pessoas Jurídicas")
        print("6 - Excluir Usuário")
        print("0 - Retornar\n")

        try:
            opcao = int(input('Escolha a opcao: '))
            if opcao in (0, 1, 2, 3, 4, 5, 6):
                return opcao
        except ValueError:
            self.mostra_mensagem('Entrada inválida.')

        return self.opcoes()

    def pega_dados_pessoa(self, tipo_pessoa):
        print('-------- DADOS USUARIO----------')
        email = input('Email: ')
        if not re.match(r'^[-\w\.]+@([\w-]+\.)+[\w-]{2,4}$', email):
            self.mostra_mensagem('EMAIL INVÁLIDO')
            return self.pega_dados_pessoa(tipo_pessoa)

        fone = input('Fone: ')
        if not re.match(r'^\(?[1-9]{2}\)? ?(?:[2-8]|9[1-9])[0-9]{3}\-?\s*?[0-9]{4}$', fone):
            self.mostra_mensagem('FONE INVÁLIDO')
            return self.pega_dados_pessoa(tipo_pessoa)

        dados = {
            'email': email,
            'fone': fone,
        }

        if tipo_pessoa == 'fisica':
            dados['nome'] = input('Nome: ')
            dados['cpf'] = input('CPF: ')
            cpf = dados['cpf']
            if not re.match(r'^[0-9]{3}.?[0-9]{3}.?[0-9]{3}-?[0-9]{2}$', cpf):
                self.mostra_mensagem('CPF INVÁLIDO')
                return self.pega_dados_pessoa(tipo_pessoa)
            dados['cpf'] = cpf.replace('.', '').replace('-', '')
        elif tipo_pessoa == 'juridica':
            dados['razao_social'] = input('Razão social: ')
            dados['cnpj'] = input('CNPJ: ')
            cnpj = dados['cnpj']
            if not re.match(r'^\d{2,3}.?\d{3}.?\d{3}/?\d{4}-?\d{2}$', cnpj):
                self.mostra_mensagem('CNPJ INVÁLIDO')
                return self.pega_dados_pessoa(tipo_pessoa)
            dados['cnpj'] = cnpj.replace('.', '').replace('-', '')

        return dados

    def mostra_pessoa(self, dados_pessoa):
        if not dados_pessoa:
            self.mostra_mensagem('Sem usuários deste tipo cadastrados.')

        for dados in dados_pessoa:
            if 'nome' in dados:
                print('NOME: ', dados['nome'])
                print('CPF: ', dados['cpf'])
            elif 'razao_social' in dados:
                print('RAZAO SOCIAL', dados['razao_social'])
                print('CNPJ', dados['cnpj'])
            print('\n')

    def pega_cadastro(self):
        cadastro = input('Entre o numero de registro (CPF/CNPJ): ')
        return cadastro.replace('-', '').replace('.', '').replace('/', '')

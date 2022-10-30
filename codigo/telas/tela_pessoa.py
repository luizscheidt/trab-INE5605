from tela import Tela

class TelaPessoa(Tela):
    def tela_opcoes(self):
        print("-------- PESSOAS----------")
        print("Escolha a opcao")
        print("1 - Cadastrar Pessoa Fisica")
        print("2 - Cadastrar Pessoa Juridica")
        print("3 - Alterar Usuário")
        print("4 - Excluir Usuário")
        print("0 - Retornar")

        try:
            opcao = int(input('Escolha a opcao: '))
        except ValueError:
            self.mostra_mensagem('Entrada inválida.')
            self.tela_opcoes()

        return opcao

    def pega_dados_pessoa(self, tipo_pessoa):
        print('-------- DADOS USUARIO----------')
        email = input('Email: ')
        fone = input('Fone: ')

        dados = {
            'email': email,
            'fone': fone,
        }

        if tipo_pessoa == 'fisica':
            dados['nome'] = input('Nome: ')
            dados['cpf'] = input('CPF: ')
        elif tipo_pessoa == 'juridica':
            dados['razao_social'] = ('Razão social: ')
            dados['cnpj'] = ('CNPJ')

        return dados

    def mostra_pessoa(self, dados_pessoa):
        if 'nome' in dados_pessoa:
            print('NOME: ', dados_pessoa['nome'])
            print('CPF: ', dados_pessoa['cpf'])
        elif 'razao_social' in dados_pessoa:
            print('RAZAO SOCIAL', dados_pessoa['razao_social'])
            print('CNPJ', dados_pessoa['cnpj'])

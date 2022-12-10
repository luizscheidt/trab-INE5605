import PySimpleGUI as sg
import re
from .tela import Tela

class TelaPessoa(Tela):
    def __init__(self):
        ...

    def init_components(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Sistema Bancário', justification= 'center' , size=(50,2))],
            [sg.Text('USUÁRIOS', size =(35,1))],
            [sg.Button('Cadastrar Pessoa Física', key='1')],
            [sg.Button('Cadastrar Pessoa Jurídica', key='2')],
            [sg.Button('Alterar Usuário', key='3')],
            [sg.Button('Listar Pessoas Físicas', key='4')],
            [sg.Button('Listar Pessoas Jurídicas', key='5')],
            [sg.Button('Listar Todos Usuários', key='6')],
            [sg.Button('Excluir Usuário', key='7')],
            [sg.Button('Retornar', key='0')],
        ]
        self.__window = sg.Window('Sistema Bancário').Layout(layout)


    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()

        return button, values

    def opcoes(self):
        self.init_components()
        button, values = self.__window.Read()

        opcao = 0
        try:
            opcao = int(button)
        except ValueError:
            pass

        self.close()

        return opcao

    def pega_dados_pessoa(self, tipo_pessoa):
        sg.theme('Reddit')

        if tipo_pessoa == 'fisica':
            cadastro = 'CPF: '
            representacao = 'Nome: '
            titulo = 'FÍSICA'
        elif tipo_pessoa == 'juridica':
            cadastro = 'CNPJ: '
            representacao = 'Razão Social'
            titulo = 'JURÍDICA'

        layout = [
            [sg.Text('-------- DADOS PESSOA %s ----------' % titulo, font=("Helvica", 25))],
            [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
            [sg.Text('Fone:', size=(15, 1)), sg.InputText('', key='fone')],
            [sg.Text(cadastro, size=(15, 1)), sg.InputText('', key='cadastro')],
            [sg.Text(representacao, size=(15, 1)), sg.InputText('', key='representacao')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema Bancário').Layout(layout)

        button, values = self.open()

        if button in (None, 'Cancelar'):
            self.close()

            return 'cancelar'

        email = values['email']
        if not re.match(r'^[-\w\.]+@([\w-]+\.)+[\w-]{2,4}$', email):
            self.mostra_mensagem('EMAIL INVÁLIDO')
            self.close()

            return self.pega_dados_pessoa(tipo_pessoa)

        fone = values['fone']
        if not re.match(r'^\(?[1-9]{2}\)? ?(?:[2-8]|9[1-9])[0-9]{3}\-?\s*?[0-9]{4}$', fone):
            self.mostra_mensagem('FONE INVÁLIDO')
            self.close()

            return self.pega_dados_pessoa(tipo_pessoa)

        dados = {
            'email': email,
            'fone': fone,
        }

        if tipo_pessoa == 'fisica':
            dados['nome'] = values['representacao']
            dados['cpf'] = values['cadastro']
            cpf = dados['cpf']

            if not re.match(r'^[0-9]{3}.?[0-9]{3}.?[0-9]{3}-?[0-9]{2}$', cpf):
                self.mostra_mensagem('CPF INVÁLIDO')
                self.close()

                return self.pega_dados_pessoa(tipo_pessoa)

            dados['cpf'] = cpf.replace('.', '').replace('-', '')
        elif tipo_pessoa == 'juridica':
            dados['razao_social'] = values['representacao']
            dados['cnpj'] = values['cadastro']
            cnpj = dados['cnpj']

            if not re.match(r'^\d{2,3}.?\d{3}.?\d{3}/?\d{4}-?\d{2}$', cnpj):
                self.mostra_mensagem('CNPJ INVÁLIDO')
                self.close()

                return self.pega_dados_pessoa(tipo_pessoa)
            dados['cnpj'] = cnpj.replace('.', '').replace('-', '')

        self.close()

        return dados

    def mostra_pessoa(self, dados_pessoa):
        if dados_pessoa:
            string_pessoas = ''
            for dados in dados_pessoa:
                if dados['tipo'] == 'fisica':
                    string_pessoas += 'Nome: ' + dados['representacao'] + '\n'
                    string_pessoas += 'CPF: ' + dados['cadastro'] + '\n'
                else:
                    string_pessoas += 'Razão Social: ' + dados['representacao'] + '\n'
                    string_pessoas += 'CNPJ: ' + dados['cadastro'] + '\n'

                string_pessoas += 'Conta: ' + dados['conta'] + '\n'
                string_pessoas += 'Fone: ' + dados['fone'] + '\n'
                string_pessoas += '------------------------------\n\n'

            sg.Popup('-------- USUÁRIOS ----------', string_pessoas)
        else:
            self.mostra_mensagem('Nenhum usuário deste tipo cadastrado.')

    def pega_cadastro(self):
        layout = [
            [sg.Text('-------- SELECIONAR USUÁRIO ----------', font=("Helvica", 25))],
            [sg.Text('Entre o numero de registro (CPF/CNPJ):', size=(35, 1)), sg.InputText('', key='cadastro')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema Bancário').Layout(layout)

        button, values = self.open()

        if button in (None, 'Cancelar'):
            self.close()

            return 'cancelar'

        cadastro = values['cadastro']

        self.close()

        return cadastro.replace('-', '').replace('.', '').replace('/', '')

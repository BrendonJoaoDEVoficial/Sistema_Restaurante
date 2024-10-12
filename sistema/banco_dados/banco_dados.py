# Curso de Desenvolvimento de Sistemas - Senac.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 13/09/2024 - 
# Objetivo: Construir uma classe responsável por gerenciar todos os dados do sistema.

import csv

class BancoDados:
    def __init__(self, objetos):
        self.objetos = [objetos]
    
    def salvar(self, caminho_arquivo, campos_arquivo, dados_arquivo):
        with open(caminho_arquivo, 'w', newline='') as arquivo_csv:
            campos = [campos_arquivo]
            escritor = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')
            escritor.writeheader()
            escritor.writerows(dados_arquivo)
     
    def ler(self, caminho_arquivo):
        informacoes = []
        with open(caminho_arquivo, 'r') as arquivo_csv:
            leitor = csv.DictReader(arquivo_csv, delimiter=';')
            for linha in leitor:
                informacoes.append(linha)
        return informacoes

    def atualizar(self, caminho_arquivo, chave_primaria, novos_valores):
        with open(caminho_arquivo, 'r') as arquivo_csv:
            leitor = csv.DictReader(arquivo_csv, delimiter=';')
            informacoes = list(leitor)
        
        for dado in informacoes:
            if dado == chave_primaria:
                # Achar forma de substituir os dados corretos.

        with open(caminho_arquivo, 'w', newline='') as arquivo_csv:
            campos = [campo for campo in arquivo_csv.readline()]
            escritor = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')
            escritor.writeheader()
            escritor.writerows(informacoes)
            
    def deletar(self, caminho_arquivo, chave_primaria):
        with open(caminho_arquivo, 'r') as arquivo_csv:
            leitura = csv.DictReader(arquivo_csv, delimiter=';')
            cadastro = list(leitura)

        # Verificando se o nome existe e apagando o registro
        apagado = False
        novo_cadastro = [registro for registro in cadastro \
            if registro['nome'] != nome_para_apagar]

        if len(novo_cadastro) < len(cadastro):
            apagado = True

        # Reescrevendo o arquivo com os dados atualizados
        with open(arquivo, 'w', newline='') as arquivo_csv:
            campos = ['nome', 'telefone', 'cidade']
            escrever = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')
            
            escrever.writeheader()
            escrever.writerows(novo_cadastro)
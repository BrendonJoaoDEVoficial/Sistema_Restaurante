# Curso de Desenvolvimento de Sistemas - Senac.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 30/09/2024 - 
# Objetivo: Construir a classe Cliente que herda a classe Usuario.

from usuario.usuario import Usuario
import os

class Cliente():
    def __init__(self):
        self.nome = ''
        self.senha = ''
        self.telefone = ''
        self.restricoes = []
    
    def criar_conta(self):
        os.system('Cls' if os.name == 'nt' else 'clear')
        print('Bem-vindo cliente!')
        print('Precisamos de algumas infromações suas para criar sua conta')
        nome = str(input('Digite seu nome: ')).strip()
        senha = str(input('Digite sua senha: ')).strip()
        confirmacao = str(input('Digite sua senha novamente: ')).strip()
        if senha != confirmacao:
            telefone = str(input('Digite seu número de telefone (+00 00 00000-0000): ')).strip()
            
            mais_restricoes = True
            restricoes = []
            contador = 0
            while mais_restricoes:
                contador += 1
                restricao = str(input(f'Digite sua {contador}º restrição alimentar: ')).strip().lower()
                restricoes.append(restricao.copy())
                mais_restricoes = str(input('Deseja adicionar outra restrição? (s/n)'))
                if mais_restricoes == 'n':
                    mais_restricoes = False
        
        self.nome = nome
        self.senha = senha
        self.telefone = telefone
        self.restricoes = restricoes
        telefone[0] != '+' and telefone[-5:-6:-1] != '-':
# Curso de desenvolvimento de Sistemas - Senac
# Turma: 0152
# Autor: Beatriz Victoria da Silva
# Data: 13/09/2024 -
# Objetivo: Construir uma Classe abstrata que servirá de modelo para as classes Cliente e Funcionario.

from abc import ABC, abstractmethod

class Usuario(ABC):
    
    @abstractmethod
    def criar_conta(self, nome, senha, telefone, tipo_usuario):
        pass
    
    @abstractmethod
    def logar(self, nome, senha):
        pass
    
    @abstractmethod
    def alterar_dados(self, dado, novo_valor):
        pass
    
    @abstractmethod
    def deletar_conta(self, conta):
        pass
    
    @abstractmethod
    def visualizar_cardapio(self, banco_dados):
        pass
    
    @abstractmethod
    def pedir(self, comprar):
        pass
    
    @abstractmethod
    def alterar_pedido(self, compra):
        pass
    
    @abstractmethod
    def finalizar(self, compra):
        pass
    
    @abstractmethod
    def entrega(self, preco):
        pass
    
    @abstractmethod
    def vizualizar_mesas(self, mesa):
        pass
    
    @abstractmethod
    def escolher_mesa(self, mesa):
        pass
    
    
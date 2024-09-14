# Curso de Desenvolvimento de Sistemas - Senac.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 13/09/2024 - 
# Objetivo: Construir uma classe responsável por gerenciar todos os dados do sistema.

import csv

class BancoDados:
    def __init__(self, objetos*):
        """Método Construtor

        Args:
            objetos (list): Lista de objetos para salvar.
        """        
        self.objetos = [objetos]
    
    def salvar(self):
        pass
    
    def ler(self):
        pass
    
    def atualizar(self, nome, dado):
        pass
    
    def deletar(self, nome):
        pass
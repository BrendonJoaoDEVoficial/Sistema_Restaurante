# Curso de Desenvolvimento de Sistemas - Senac.
# Turma: 0152.
# Autor: Brendon João Campos Neves.
# Data: 13/09/2024 - 
# Objetivo: Construir uma classe responsável por gerenciar todos os dados do sistema.

import csv

class BancoDados:
    def __init__(self, objetos):
        """Método Construtor

        Args:
            objetos (list): Lista de objetos para salvar.
        """        
        self.objetos = [objetos]
    
    def salvar(self,dados_novos, caminho):
        if caminho:
            with open(caminho, 'r') as arquivo_lido:
                leitor = csv.DictReader(arquivo_lido, delimiter=';')
                dados_existentes = list(leitor)
            
            dados_totais = dados_existentes.extend(dados_novos)
            
            with open(caminho, 'w', newlines='') as arquivo_atual:
                campos = []
                for dados in dados_totais:
                    for chave in dados.keys():
                        if chave not in campos:
                            campos.append(chave)
                
                escritor = csv.DictWriter(arquivo_atual, fieldnames=campos, delimiter=';')
                
                escritor.writeheader()
                
                escritor.writerows(dados_totais)
                    
    def ler(self):
        pass
    
    def atualizar(self, nome, dado):
        pass
    
    def deletar(self, nome):
        pass
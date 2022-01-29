############################################################
## Dados da Equipe                                        ##
############################################################

############################################################
## Aluno: Gabriel Pereira Silva                           ##
## COMP0334 - PROGRAMAÇÃO IMPERATIVA (2020.2 - TURMA-T11) ##
############################################################

############################################################
# Arquivos com bibliotecas definidas pelo(a) programador(a)#
############################################################

import emoji
import graph_linha
import graph_barras


############################################################
# Interface de interação com o usuário                     #
############################################################

print(emoji.emojize('Seja Bem-vindo! Voçê tem 2 opções de Gráficos::sunglasses:', use_aliases=True))
print('1: Gráfico de linha')
print('2: Gráfico de barras')
class var:
    def __init__(self):
        self.entrada = int(input('Digite 1 ou 2: '))
        ############################################################
        while True:  # laço para escolher opção de gráfico 1 ou 2.

            if self.entrada == 1:
                graph_linha.apresentarGraficoDeLinha()
                break

            elif self.entrada == 2:
                graph_barras.apresentarGragicodeBarras()
                break

            else:
                self.entrada = int(input('Digite um numero entre 1 e 2: '))
                continue
var()

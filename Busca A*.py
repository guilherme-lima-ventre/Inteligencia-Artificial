from random import shuffle, randrange
import numpy as np
import time 

def cria_labirinto(larg, alt):
  lab = [[0] * larg + [1] for _ in range(alt)] + [[1] * (larg + 1)]
  semMuros = []

  def quebra_muros(lin, col):
    lab[lin][col] = 1
    direcao = [(lin, col + 1), (lin, col - 1), (lin - 1, col), (lin + 1, col)]
    shuffle(direcao)

    for (l, c) in direcao:
      if lab[l][c] != 1:
        semMuros.append((lin, col, l, c)) 
        quebra_muros(l, c)
        
  quebra_muros(randrange(alt), randrange(larg))
  return semMuros

def desenha_labirinto(lab, larg, alt):
  vertical = [['|   '] * larg + ['|'] for _ in range(alt)] + [[]]
  horizontal = [['+---'] * larg + ['+'] for _ in range(alt + 1)]

  matriz = [[1] * (larg * 2 + 1) for i in range(alt * 2 + 1)]
  for i in range(alt * 2 + 1):
    for j in range(larg * 2 + 1):
      if i % 2 != 0 and j % 2 != 0:
        matriz[i][j] = 0 
  
  for (l1, c1, l2, c2) in lab:
    if l1 == l2:
      vertical[l1][max(c1, c2)] = '    '
      matriz[l1 * 2 + 1][max(c1, c2) * 2] = 0
    if c1 == c2:
      horizontal[max(l1, l2)][c1] = '+   ' 
      matriz[max(l1, l2) * 2][c1 * 2 + 1] = 0
  
  for (a, b) in zip(horizontal, vertical):
    print(''.join(a + ['\n'] + b))

  return matriz

def a_estrela(matriz, ini, obj):
  inicio = (ini[0] * 2 + 1, ini[1] * 2 + 1)
  fim = (obj[0] * 2 + 1, obj[1] * 2 + 1)
  caminho = [inicio], funcao = [], direcoes = []
  g = 0
  
#a gente tem uma noção de quantas vezes vamos fazer por conta do calculo de heuristica inicial, ta faltando considerar isso. 
#

  while caminho[-1] != fim:
    filhos = nos_filhos(matriz, caminho[-1], fim)
    funcao.append(list()), direcoes.append(list())
    g += 2
    for i in enumerate(filhos):
      direcoes[-1].append(filhos[i])
      funcao[-1].append(abs(filhos[i][0] - fim[0]) + abs(filhos[i][1] - fim[1]) + g)

    f_min = min(funcao)
    next = direcoes[-1][funcao.index(f_min)]
    funcao[-1].remove(f_min)
    direcoes[-1].remove(next)
    
    caminho.append(next)

def nos_filhos(matriz, posicao, fim):
  direcoes= [(posicao[0], posicao[1] + 1), (posicao[0] - 1, posicao[1]), (posicao[0], posicao[1] - 1), (posicao[0] + 1, posicao[1])]
  i = 0
  for (l, c) in direcao:
      if lab[l][c] == 1:
        del(direcoes[i])
      i += 1
  return direcoes


alt = int(input('Indique a altura do labirinto: '))
larg = int(input('Indique a largura do labirinto: '))

lab = cria_labirinto(alt, larg)
a_estrela(desenha_labirinto(lab), (randrange(alt), randrange(larg)), (randrange(alt), randrange(larg))

'''
def a_estrela(lab, ini, obj):

#retornar nós visitados e suas f's
#retornar o próprio caminho






Segunda função: parametros G da posição (acima) e as posições filhas
a função irá calcular a f (soma da g e h) das filhas, isso me ajudará a decidir qual o caminho de menor custo. 
A G das filhas é a G da posição + 2.


A heuristica e o custo são sempre recalculados. A minha função tem que calcular o caminho ideal 
 


def funcao_filhos(g, filhos):



#def aEstrela(lab, inicio, fim):
  #retornar nós visitados e suas f's 
  #retornar o proprio caminho, n sei como mas queria ir printando o percurso que ele faz, mas quero atualizar o mapa toda vez que ele faz isso
# Já sei pq eu sou demais end='\r'

#1º calcula a distancia ideal do ponto I ate o ponto F
  #(|x1 - x2| + |y1 - y2|) - essa é a distancia ideal
  
#2º escolher a proxima posição baseado no valor da distancia de cada possivel ponto

# print('\U0001F47E') -- para printar o ponto se movendo

'''
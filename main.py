from random import shuffle, randrange
import time 

def criaLabirinto(larg, alt):
  lab = [[0] * larg + [1] for _ in range(alt)] + [[1] * (larg + 1)]
  semMuros = []

  def quebraMuros(lin, col):
    lab[lin][col] = 1
    direcao = [(lin, col + 1), (lin, col - 1), (lin - 1, col), (lin + 1, col)]
    shuffle(direcao)

    for (l, c) in direcao:
      if lab[l][c] != 1:
        semMuros.append((lin, col, l, c)) 
        quebraMuros(l, c)
        
  quebraMuros(randrange(alt), randrange(larg))
  return semMuros

def desenhaLabirinto(lab, larg, alt):
  vertical = [['|   '] * larg + ['|'] for _ in range(alt)] + [[]]
  horizontal = [['+---'] * larg + ['+'] for _ in range(alt + 1)]

  for (l1, c1, l2, c2) in lab:
    if l1 == l2:
      vertical[l1][max(c1, c2)] = '    '
    if c1 == c2:
      horizontal[max(l1, l2)][c1] = '+   '
  
  for (a, b) in zip(horizontal, vertical):
    print(''.join(a + ['\n'] + b))

#def aEstrela(lab, inicio, fim):
  #retornar nós visitados e suas f's 
  #retornar o proprio caminho, n sei como mas queria ir printando o percurso que ele faz, mas quero atualizar o mapa toda vez que ele faz isso

#1º calcula a distancia ideal do ponto I ate o ponto F
  #(|x1 - x2| + |y1 - y2|) - essa é a distancia ideal
  
#2º escolher a proxima posição baseado no valor da distancia de cada possivel ponto
desenhaLabirinto(criaLabirinto(9, 9), 9, 9)

# print('\U0001F47E') -- para printar o ponto se movendo



from random import shuffle, randrange

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

def desenha_labirinto(lab, alt, larg):
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
  caminho = list()
  caminho.append(inicio)
  visitados = list()
  funcao = list()
  direcoes = list()
  g = 0
  retroceder = list()
  retroceder.append(0)
  print("Inicio =", inicio, "\nFim =", fim, "\n")

  while caminho[-1] != fim:
    if caminho[-1] == inicio:
      filhos = nos_filhos(matriz, caminho[-1], caminho[-1], fim)
    else:
      filhos = nos_filhos(matriz, caminho[-1], caminho[-2], fim)
    
    if filhos == None: 
      for i in range(0, retroceder[-1] + 1):
        del caminho[-1]
        g -= 2
      del retroceder[-1]
    else:
      funcao.append(list()), direcoes.append(list())
      g += 2
      for i in range(0, len(filhos)):
        direcoes[-1].append(filhos[i])
        funcao[-1].append(abs(filhos[i][0] - fim[0]) + abs(filhos[i][1] - fim[1]) + g)

    f_min = min(funcao[-1])
    next = direcoes[-1][funcao[-1].index(f_min)]
    funcao[-1].remove(f_min)
    direcoes[-1].remove(next)
    if funcao[-1] == []:
      retroceder[-1] += 1
      del funcao[-1]
      del direcoes[-1]
    else:
      retroceder.append(0)
    filhos = None
    visitados.append([next, f_min])
    caminho.append(next)

  print("Pontos visitados:\n")
  j = 0
  for i in visitados:
    j += 1
    print(i, end=' ')
    if(j % 4 == 0):
      print()
  if(j % 4 != 0):
    print()
  print("\nCaminho percorridos:\n", caminho)

def nos_filhos(matriz, posicao, anterior, fim):
  direcoes = [(posicao[0], posicao[1] + 2), (posicao[0] - 2, posicao[1]), (posicao[0], posicao[1] - 2), (posicao[0] + 2, posicao[1])]
  i = 0

  if posicao[0] == anterior[0] and posicao[1] == anterior[1] - 2 or matriz[posicao[0]][posicao[1] + 1] == 1:
    del(direcoes[i]) #direita
  else:
    i += 1
  if posicao[0] == anterior[0] + 2 and posicao[1] == anterior[1] or matriz[posicao[0] - 1][posicao[1]] == 1:
    del(direcoes[i]) #pra cima
  else:
    i += 1
  if posicao[0] == anterior[0] and posicao[1] == anterior[1] + 2 or matriz[posicao[0]][posicao[1] - 1] == 1:
    del(direcoes[i])  #esquerda
  else:
    i += 1
  if posicao[0] == anterior[0] - 2 and posicao[1] == anterior[1] or matriz[posicao[0] + 1][posicao[1]] == 1:
    del(direcoes[i]) #baixo
  else:
    i += 1
  
  if i == 0:
    return None
  return direcoes

alt = int(input('Indique a altura do labirinto: '))
larg = int(input('Indique a largura do labirinto: '))
inicio = (randrange(alt), randrange(larg))
fim = (randrange(alt), randrange(larg))
while inicio == fim:
  inicio = (randrange(alt), randrange(larg))
  fim = (randrange(alt), randrange(larg))

lab = cria_labirinto(larg, alt)
a_estrela(desenha_labirinto(lab, alt, larg), inicio, fim)
def iniciar():
  return [[' '] * 3 for _ in range(3)]

def desenhar(estado):
  for i in range(3):
    print('|', end = '')
    for j in range(3):
      print('{}|'.format(estado[i][j]), end ='')
    print()
  print()

#retorna:
#'x' se x ganhou
#'o' se o ganhou
#'-' se empatou
#' ' se não acabou
def acabou(estado):
  #checando vitorias horizontais e verticais
  for i in range(3):
    if estado[i] == ['x'] * 3:
      return 'x'
    if estado[i] == ['o'] * 3:
      return 'o'
    if estado[0][i] != ' ' and estado[0][i] == estado[1][i] and estado[1][i] == estado[2][i]:
      return estado[0][i]
    
  #checando a diagonal principal
  if estado[0][0] != ' ' and estado[0][0] == estado[1][1] and estado[1][1] == estado[2][2]:
    return estado[0][0]

  #checando a diagonal invertida
  if estado[0][2] != ' ' and estado[0][2] == estado[1][1] and estado[1][1] == estado[2][0]:
    return estado[0][2]

  if ' ' in estado[0] + estado[1] + estado[2]:
    return ' '

  return '-'

#retorna uma tupla sendo o:
#1o valor: pontuação do estado
#2o valor: posição da jogada que resulta na pontuação do 1o valor
def jog_max(estado):
  final = acabou(estado)
  if final == 'x':
    return(1, (-1, -1))
  if final == 'o':
    return(-1, (-1, -1))
  if final == '-':
    return(0, (-1, -1))

  maior = -2 #
  for i in range(3):
    for j in range(3):
      if estado[i][j] == ' ':
        estado[i][j] = 'x' #
        (pontuacao, (jog_x, jog_y)) = jog_min(estado)
        if pontuacao > maior: #
          maior = pontuacao
          melhor_jogada = (i, j)
        estado[i][j] = ' '

  return(maior, melhor_jogada)

def jog_min(estado):
  final = acabou(estado)
  if final == 'x':
    return(1, (-1, -1))
  if final == 'o':
    return(-1, (-1, -1))
  if final == '-':
    return(0, (-1, -1))

  menor = 2 
  for i in range(3):
    for j in range(3):
      if estado[i][j] == ' ':
        estado[i][j] = 'o' 
        (pontuacao, (jog_x, jog_y)) = jog_max(estado)
        if pontuacao < menor: 
          menor = pontuacao
          melhor_jogada = (i, j)
        estado[i][j] = ' '

  return(menor, melhor_jogada)

def jogar_ia_vs_ia():
  jogo = iniciar()
  res = ' '
  turno = 0
  while res == ' ':
    desenhar(jogo)
    if turno % 2 == 0:
      #jogada do 'x'
      (ponto, (x, y)) = jog_max(jogo)
      jogo[x][y] = 'x'
    else:
      #jogada do 'o'
      (ponto, (x, y)) = jog_min(jogo)
      jogo[x][y] = 'o'
    turno += 1
    res = acabou(jogo)
  desenhar(jogo)
  #quem ganhou
  switch = {
    'x': "Jogador X ganhou!\n",
    'o': "Jogador O ganhou!\n",
    '-': "O jogo empatou!\n"
  }
  print(switch.get(res))
  
def jogar_ia_vs_humano():
  jogo = iniciar()
  res = ' '
  turno = 0
  #receber figura do humano
  humano = input("Escolha sua figura, 'x' ou 'o': ").lower()
  print()
  while humano not in ['x', 'o']:
    humano = input("Opcao invalida, tente novamente.\nEscolha sua figura, 'x' ou 'o': ").lower()
    print()
  
  if humano == 'x':
    while res == ' ':
      desenhar(jogo)
      if turno % 2 == 0:
        #jogada humano
        x, y = input("Digite a posicao que deseja jogar [linha coluna]: ").split(' ')
        print()
        while (int(x) < 0 or int(x) > 2) or (int(y) < 0 or int(y) > 2) or jogo[int(x)][int(y)] != ' ':
          x, y = input("Posicao invalida, tente novamente.\nDigite a posicao que deseja jogar [linha coluna]: ").split(' ')
          print()
        jogo[int(x)][int(y)] = 'x'
      else:
        #jogada IA
        (ponto, (x, y)) = jog_min(jogo)
        jogo[x][y] = 'o'
      turno += 1
      res = acabou(jogo)
    switch = {
      'x': "Voce ganhou!\n",
      'o': "A IA ganhou!\n",
      '-': "O jogo empatou!\n"
    } 
  else:
    while res == ' ':
      desenhar(jogo)
      if turno % 2 == 0:
        #jogada IA
        (ponto, (x, y)) = jog_max(jogo)
        jogo[x][y] = 'x'
      else:
        #jogada humano
        x, y = input("Digite a posicao que deseja jogar [linha coluna]: ").split(' ')
        print()
        while (int(x) < 0 or int(x) > 2) or (int(y) < 0 or int(y) > 2) or jogo[int(x)][int(y)] != ' ':
          x, y = input("Posicao invalida, tente novamente.\nDigite a posicao que deseja jogar [linha coluna]: ").split(' ')
          print()
        jogo[int(x)][int(y)] = 'o'
      turno += 1
      res = acabou(jogo)
    switch = {
      'x': "A IA ganhou!\n",
      'o': "Voce ganhou!\n",
      '-': "O jogo empatou!\n"
    }
  desenhar(jogo)
  print(switch.get(res))


jogar_ia_vs_ia()
jogar_ia_vs_humano()


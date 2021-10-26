def iniciar():
  return [[' '] * 3 for _ in range(3)]

def desenhar(estado):
  for i in range(3):
    print('|', end = '')
    for j in range(3):
      print('{}|'.format(estado[i][j]), end ='')
    print()
  print()

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

def jogar_ia_vs_ia():
  jogo = iniciar()
  res = ' '
  turno = 0
  while res == ' ':
    desenhar(jogo)
    if turno % 2 == 0:
      #jogada do 'x'
      (ponto, (x, y)) = jog_max_alpha_beta(jogo)
      jogo[x][y] = 'x'
    else:
      #jogada do 'o'
      (ponto, (x, y)) = jog_min_alpha_beta(jogo)
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
        (ponto, (x, y)) = jog_min_alpha_beta(jogo)
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
        (ponto, (x, y)) = jog_max_alpha_beta(jogo)
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

def jog_max_alpha_beta(estado, alfa = -2, beta = 2):
  final = acabou(estado)
  if final == 'x':
    return (1, (-1, -1))
  elif final == 'o':
    return (-1, (-1, -1))
  elif final == '-':
    return (0, (-1, -1))

  max_valor = -2
  melhor_jogada = (-1, -1)
  for i in range(3):
    for k in range(3):
      if estado[i][k] == ' ':
        estado[i][k] = 'x'
        (valor, (x, y)) = jog_min_alpha_beta(estado, alfa, beta)
        if valor > max_valor:
          melhor_jogada = (i, k)
          max_valor = valor
        alfa = max(alfa, valor)
        estado[i][k] = ' '
        if beta <= alfa:
          break

  return max_valor, melhor_jogada
   

def jog_min_alpha_beta(estado, alfa = -2, beta = 2):
  final = acabou(estado)
  if final == 'x':
    return (1, (-1, -1))
  elif final == 'o':
    return (-1, (-1, -1))
  elif final == '-':
    return (0, (-1, -1))

  min_valor = 2
  melhor_jogada = (-1, -1)
  for i in range(3):
    for k in range(3):
      if estado[i][k] == ' ':
        estado[i][k] = 'o'
        (valor, (x, y)) = jog_max_alpha_beta(estado, alfa, beta)
        if valor < min_valor:
          melhor_jogada = (i, k)
          min_valor = valor
        beta = min(beta, valor)
        estado[i][k] = ' '
        if beta <= alfa:
          break

  return min_valor, melhor_jogada

jogar_ia_vs_ia()
jogar_ia_vs_humano()
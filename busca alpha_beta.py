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

def heuristica(estado):
   vitorias_x = 0
   vitorias_o = 0

   for i in range(3):
      if 'o' not in estado[i]:
         vitorias_x += 1
         vitorias_x += estado[i].count('x')
      if 'x' not in estado[i]:
         vitorias_o += 1
         vitorias_o += estado[i].count('o')
      if 'o' not in [estado[0][i], estado[1][i], estado[2][i]]:
         vitorias_x += 1
         for k in range(3):
           if estado[k][i] == 'x':
             vitorias_x += 1
      if 'x' not in [estado[0][i], estado[1][i], estado[2][i]]:
         vitorias_o += 1
         for k in range(3):
           if estado[k][i] == 'o':
             vitorias_o += 1
         
   #checando a diagonal principal
   if estado[0][0] != 'o' and estado[1][1] != 'o' and estado[2][2] != 'o':
      vitorias_x += 1
      for k in range(3):
        if estado[k][k] == 'x':
          vitorias_x += 1
   if estado[0][0] != 'x' and estado[1][1] != 'x' and estado[2][2] != 'x':
      vitorias_o += 1
      for k in range(3):
        if estado[k][k] == 'o':
          vitorias_o += 1

   if estado[0][2] != 'o' and estado[1][1] != 'o' and estado[2][0] != 'o':
      vitorias_x += 1
      for k in range(3):
        if estado[k][2 - k] == 'x':
          vitorias_x += 1
   if estado[0][2] != 'x' and estado[1][1] != 'x' and estado[2][0] != 'x':
      vitorias_o += 1
      for k in range(3):
        if estado[k][2 - k] == 'o':
          vitorias_o += 1

   return vitorias_x - vitorias_o


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
    'x': "Jogador X ganhou!",
    'o': "Jogador O ganhou!",
    '-': "O jogo empatou!"
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
      'x': "Voce ganhou!",
      'o': "A IA ganhou!",
      '-': "O jogo empatou!"
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
      'x': "A IA ganhou!",
      'o': "Voce ganhou!",
      '-': "O jogo empatou!"
    }
  desenhar(jogo)
  print(switch.get(res))

def jog_max_alpha_beta(estado, alfa = -100, beta = 100):
  final = acabou(estado)
  if final != ' ':
    return heuristica(estado)
    

  for i in range(3):
    for k in range(3):
      if estado[i][k] == ' ':
        estado[i][k] = 'x'
        valor = jog_min_alpha_beta(estado)
        if valor > 
                h = heuristica(estado)
        jogada_h = (i, k)

  return h #pq se não for o ultimo e não me der o valor final eu quero o valor de h pra saber se ele é melhor ou nao que alfa e beta
  eu quero todos os H finais e vou comparar eles, ai eu gostaria de eliminar tudo abaixo KKKKKKKK pra poder fazer com que a linha acima dos finais 
  seja agora o final, com os valores das heuristicas do que eram os nos filhos
   

def jog_min_alpha_beta(estado, alfa = -100, beta = 100):
  final = acabou(estado)
  if final != ' ':
    return heuristica(estado)

  for i in range(3):
    for k in range(3):
      if estado[i][k] == ' ':
        estado[i][k] = 'o'
        jog_max_alpha_beta(estado)

jogar_ia_vs_ia()
jogar_ia_vs_humano()
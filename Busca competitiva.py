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

  menor = 2 #
  for i in range(3):
    for j in range(3):
      if estado[i][j] == ' ':
        estado[i][j] = 'o' #
        (pontuacao, (jog_x, jog_y)) = jog_max(estado)
        if pontuacao < menor: #
          menor = pontuacao
          melhor_jogada = (i, j)
        estado[i][j] = ' '

  return(menor, melhor_jogada)

#def jogar_ia_vs_ia():

#def jogar_ia_vs_humano():

#def jog_max_alpha_beta():

#def jog_min_alpha_beta():

#def jog_min(estado):
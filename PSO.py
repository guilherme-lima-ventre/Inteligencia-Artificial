import labirinto as lb
import numpy as np
from pyswarm import pso

larg = 4
alt = 3
inicio = (0, 0)
obj = (alt - 1, larg - 1)
sem_muros = lb.cria_labirinto(larg, alt)
lb.desenha_labirinto(lab = sem_muros, larg = larg, alt = alt)

sol_tam = (larg * alt - 1) * 2

def aptidao(solucao):
  def calc_vizinho(pos, direcao):
    if direcao == (1, 1):
      return(pos[0] - 1, pos[1])
    elif direcao == (0, 0):
      return(pos[0] + 1, pos[1])
    elif direcao == (0, 1):
      return(pos[0], pos[1] + 1)
    elif direcao == (1, 0):
      return(pos[0], pos[1] - 1)
  
  i = 0
  while i < len(solucao):
    if solucao[i] <= 0.5:
      solucao[i] = 0
    else:
      solucao[i] = 1
    i += 1
  atual = inicio
  i = 0
  while i < (sol_tam - 1) and atual != obj:
    direcao = (solucao[i], solucao[i + 1])
    vizinho = calc_vizinho(atual, direcao)
    if atual + vizinho in sem_muros or vizinho + atual in sem_muros:
      atual = vizinho
    i += 2

  return abs(atual[0] - obj[0]) + abs(atual[1] - obj[1])

'''' 
  Documentação
    pso(func, lb, ub, ieqcons=[], f_ieqcons=None, args=(), kwargs={},
    swarmsize=100, omega=0.5, phip=0.5, phig=0.5, maxiter=100, minstep=1e-8,
    minfunc=1e-8, debug=False)
'''
minimo = np.array([0] * sol_tam)
maximo = np.array([1] * sol_tam)

caminho, valor = pso(aptidao, minimo, maximo, swarmsize=100, maxiter=100)

print("Caminho: " + str(caminho))
print("Aptidao: " + str(valor))

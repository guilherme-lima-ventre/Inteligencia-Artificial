import labirinto as lb
from geneticalgorithm import geneticalgorithm as ga
import numpy as np
import random
import math

larg = 4
alt = 3
inicio = (0, 0)
obj = (alt - 1, larg - 1)
caminho = list()

sem_muros = lb.cria_labirinto(larg, alt)
lb.desenha_labirinto(lab = sem_muros, larg = larg, alt = alt)

#direções: (11, 00, 01, 10) -> (N, S, L, O)
#exemplo:
#+--+--+--+
#| i      |
#+--+--+  +
#|       o|
#+--+--+--+
#solução: 010100...
#+--+--+--+
#| i      |
#+--+--+  +
#| o      |
#+--+--+--+
#solução: 0101001010

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

  def custo(posicao):
    return (abs(posicao[0] - obj[0]) + abs(posicao[1] - obj[1]))

  atual = inicio
  distancia = sol_tam
  i = 0


  while i < (sol_tam - 1) and atual != obj:
    direcao = (solucao[i], solucao[i + 1])
    vizinho = calc_vizinho(atual, direcao)
    dif_custo = custo(direcao) - custo(vizinho) 
    if atual + vizinho in sem_muros or vizinho + atual in sem_muros:
      if dif_custo > 0:
        atual = vizinho
      else:
        if random.uniform(0, 1) < math.exp(-dif_custo / distancia):
          atual = vizinho
    distancia -= 1

    i += 2

  return(abs(atual[0] - obj[0]) + abs(atual[1] - obj[1]))

#exemplo:
#+--+--+--+
#| i      |
#+  +--+  +
#|  |    o|
#+--+--+--+
# aptidao([0,1,0,0,1,1,0,0,1,0])
# 3
# Documentacao
#geneticalgorithm(function, dimension, variable_type='bool', variable_boundaries=None, variable_type_mixed=None, function_timeout=10, algorithm_parameters={'max_num_iteration': None,\ 'population_size':100,\ 'mutation_probability':0.1,\ 'elit_ratio': 0.01,\ 'crossover_probability': 0.5,\ 'parents_portion': 0.3,\ 'crossover_type':'uniform',\ 'max_iteration_without_improv':None}, convergence_curve=True, progress_bar=True)

parametros = {'max_num_iteration': 5,
 'population_size':5,
 'mutation_probability':0.01,
 'elit_ratio': 0.1,
 'crossover_probability': 0.5, 
 'parents_portion': 0.3, 
 'crossover_type':'one_point',
 'max_iteration_without_improv': 10}

exp = ga(aptidao, sol_tam, 'int', np.array([[0, 1]] * sol_tam), algorithm_parameters = parametros)

exp.run()

#Atividade:
#1. variar parametros do problema
#2. resolver com Simulated Annealing
#3. resolver com PSO
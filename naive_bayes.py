from sklearn.datasets import load_iris, load_wine
from sklearn.naive_bayes import GaussianNB
from mlxtend.feature_selection import SequentialFeatureSelector as SFS

# Implementar o Naive Bayes Wrapper;
# Testar com a Iris e alguma outra base de dados da sua escolha:

colunas_iris = load_iris().feature_names
colunas_wine = load_wine().feature_names
# Implementamos utilizando mlxtend, mais especificamente um seletor sequencial
# Usando o banco de dados iris
X, y = load_iris(return_X_y = True)
sfs1 = SFS(GaussianNB(), (1, len(X[0])), forward=True, cv=0)
sfs1.fit(X, y)
print(f"A precisão do SFS para iris é de {(sfs1.k_score_).round(4)}.")
colunas_sfs1 = list()
for i in range(len(colunas_iris)):
  if str(i) in sfs1.k_feature_names_:
    colunas_sfs1.append((colunas_iris[i], i))
print(f"O melhor subset para previsão utiliza as colunas ('nome', indice):\n{colunas_sfs1}.\n")

# Usando o banco de dados wine
W, z = load_wine(return_X_y = True)
sfs2 = SFS(GaussianNB(), (1, len(W[0])), forward=True, cv=0)
sfs2.fit(W, z)
print(f"A precisão do SFS para wine é de {(sfs2.k_score_).round(4)}.")
colunas_sfs2 = list()
for i in range(len(colunas_wine)):
  if str(i) in sfs2.k_feature_names_:
    colunas_sfs2.append((colunas_wine[i], i))
print(f"O melhor subset para previsão utiliza as colunas ('nome', indice):\n{colunas_sfs2}.")

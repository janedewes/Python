
"""
Na REGRESSÃO queremos achar um fç que melhor descreve o comportamento dos dados, essa fç assume valores contínuos.
Na CLASSIFICAÇÃO a nossa variável Target (alvo) é uma classe (discreta)

"""

import numpy as np


#Dados do segundo capítulo
x = [-1., -0.77777778, -0.55555556, -0.33333333, -0.11111111, 0.11111111, 0.33333333, 0.55555556, 0.77777778, 1.]
y = [-1.139556201, -0.57177999, -0.21697033, 0.5425699, 0.49406657, 1.14972239, 1.64228553, 2.1749824, 2.64773614, 2.95684202]

#plot dos dados:
plt.figure(figsize=(10, 5))
plt.plot(x, y, 'o', label='dados originais') #tirando o 'o' ele traça um gráfico de linha!
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()

#transformando em numpy array
x, y = np.array(x).reshape(-1, 1), np.array(y).reshape(-1, 1)

#modelo
from sklearn.linear_model import LinearRegression

#treinando o modelo: y = a*x + b, valores reais (a, b) = (2, 1) (treinar modelo de regressao = estimar a e b)
reg = LinearRegression()
reg.fit(x, y)

#Coef a, b estimados:
#valores estimados usando o numpy diretamente
# a estimado no numpy: 2.05414951
# b estimado no numpy: 0.96798926
print("a estimado:", reg.coef_.ravel()[0])
print("b estimado:", reg.intercept_[0])
#Os valores conferem!!!!!


# predição do modelo  (aumentar a quantidade de dados)
y_pred = reg.predict(x)

#score do modelo  (metrica p saber o quão bom/ruim foi o modelo p uma determinada base de dados)
score = reg.score(x, y)
print("score", score)

#plot dos dados
plt.figure(figsize=(10, 5))
plt.plot(x, y, 'o', label='dados originais') #tirando o 'o' ele traça um gráfico de linha!
plt.plot(x, y_pred, label='regressão linear (R2: {:.3f})'.format(score)) #R2 reta da regressão
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Regressão linear no scikit-learn")
plt.grid()
plt.show()


"""
Conceitos básicos de RL
- Problema: dado um conjunto de pontos, achar qual a função que melhor descreve esses pontos
- Um critério comumente usado é o erro quadrático, que queremos minimizar.
- Com o critério definido e, sabendo que a fç linear possui o seguinte formato: y = f(x) = ax + b
- O problema de regressão resume-se à determinação dos coeficientes a e b, visto que x e y são dados de entrada.

-Matricialmente:

(X^T * X)^-1 * X^T * y
"""
#visualização de dados
import matplotlib.pyplot as plt

import numpy as np

#dados
x = [-1., -0.77777778, -0.55555556, -0.33333333, -0.11111111, 0.11111111, 0.33333333, 0.55555556, 0.77777778, 1.]
y = [-1.139556201, -0.57177999, -0.21697033, 0.5425699, 0.49406657, 1.14972239, 1.64228553, 2.1749824, 2.64773614, 2.95684202]


""" OBS: só comentei o plot para gerar os valores de a e b, abaixo!!! (descomentar para ver o plot)

#plot dos dados:
plt.figure(figsize=(10, 5))
plt.plot(x, y, 'o', label='dados originais') #tirando o 'o' ele traça um gráfico de linha!
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
"""

"""
- Regressão linear: Solução via minimização do erro quadrático, onde usamos a pseudo-inversa de X, calculada pelo método "np.linalg.pinv(X)".

Estimar um fç do tipo y = f(x) = ax + b
ou seja, achar os valores de a e b,
que melhor representam os dados: 

Os valores reais de a e b são: (a, b): 2, 1 
"""

#transformando para numpy e vetor coluna:
x, y = np.array(x).reshape(-1, 1), np.array(y).reshape(-1, 1)

#add bias: para estimar o termo b: (add colunas de 1´s, por causa do b da equação 1*b) (sempre que estiver só uma letra add essa matriz ones)
X = np.hstack((x, np.ones(x.shape)))
#concatenou x com a coluna de 1´s


#estimando a e b:
beta = np.linalg.pinv(X).dot(y)
print("a estimado:", beta[0][0])
print("b estimado:", beta[1][0])
#OBS: dados muito próximos dos valores de a e b!!!!

#Plot dos dados
plt.figure(figsize=(10, 5))
plt.plot(x, y, 'o', label='dados originais')
plt.plot(x, X.dot(beta), label='regressão linear') #reta da fç estimada acima!!! (possui o menor erro quadrático possível)
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.sho

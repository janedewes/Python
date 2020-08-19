"""
Dicas e métodos de Numpy 
"""

import numpy as np

print('------------------------1---------------------------')
#array
x = np.array([[1, 3, 7],
              [4, 11, 21],
              [42, 8, 9]])
print("x: \n", x)


print('------------------------2---------------------------')
#reshape: transformar a matriz em vetor coluna (3, 3) vira (9, 1): 3*3 = 9*1 = 9
print("transformação de um vetor coluna: \n", x.reshape(9, 1))
print("transformação de um vetor linha: \n", x.reshape(1, 9)) #ou outro exemplo



print('------------------------4---------------------------')
#transposição da matriz
print("x transposta: \n", x.T)

print('------------------------5---------------------------')
#np.sum: soma em um dado eixo, axis = {0: linha, 1:coluna}
print("x: \n", x)
print("soma de todos os elementos de x: \n", np.sum(x))
print("soma de x ao longo das linhas: \n", np.sum(x, axis=0))
print("soma de x ao longo das colunas: \n", np.sum(x, axis=1))

print('------------------------6---------------------------')
#np.mean: media em um dado eixo, axis = {0: linha, 1:coluna}
print("x: \n", x)
print("media de todos os elementos de x: \n", np.mean(x))
print("media de x ao longo das linhas: \n", np.mean(x, axis=0))
print("media de x ao longo das colunas: \n", np.mean(x, axis=1))

#mediana: np.median

print('------------------------7---------------------------')
#np.where, identificação dos índices onde uma dada condição é atendida. Uso conjunto com indexação booleana:
cond = x % 2 == 0 #numeros pares
print("condição: \n", cond)
i, j = np.where(cond) # índices x[i, j] = x[cond]
print("índice i (linhas):", i)
print("indice j (colunas):", j)


print('------------------------8---------------------------')
#indexação booleana e slicing: selecionar as linhas de x que possuem algum numero par
print("x: \n", x)
cond = x % 2 == 0 #números pares
print("condição: \n", cond)

#se houver alguma condição True na linha, a soma será > 0
i_row = np.where(np.sum(cond, axis=1))[0]
print("indices das linhas que possuem números pares:", i_row)
print("linhas que possuem números pares: \n", x[i_row, :])


print('------------------------FIM---------------------------')
"""
Introdução as arrays

- Numpy é uma das principais bibliotecas para computação científica em PY
- Ele disponibiliza um objeto de array multidimensional de alta performance e diversas ferramentas para trabalhar com esses objetos.
- Estrutura de dados para manipulação e algebra matricial, possibilita trabalhar com estruturas de dados n-dimensionais

EX: Shape: (quantidade de elementos em cada eixo)
1D) shape:(4,)
_ _ _ _

2D) shape:(2,3)
_ _ _ 
_ _ _

3D) shape:(4,3,2)
_ _ _
_ _ _
_ _ _
_ _ _ OBS: profundidade:2

AXIS: direção ao longo do eixo: (x,y,z)
 axis 0 (ao longo das linhas)
 axis 1 (ao longo das colunas)
 axis 3 (ao longo de "Z")
"""

#importando as bibliotecas (File, Settings, Project, Project:Interpreter +)
import numpy as np

#help(mp.array)

#criação de um array 1D: [1, 2, 3]
print('---------- Criação de array 1D ---------- ')
l = [1, 2, 3]
x = np.array(l)
print("x:", x)
print("shape", x.shape)


#criação de um array 2D: listas aninhadas
print('---------- Criação de array 2D ---------- ')
l = [[1, 2], [3,4]]
x = np.array(l)
print("x:\n", x)
print("shape:", x.shape)

#Array contendo apenas 0's
print('---------- Array contendo apenas 0s ---------- ')
dim = (4, 4) #(linhas, colunas)
x = np.zeros(dim)
print("x:\n", x)
print("shape:", x.shape)

#Array contendo apenas 1's
print('---------- Array contendo apenas 1s ---------- ')
dim = (10, 10) #(linhas, colunas)
x = np.ones(dim)
print("x:\n", x)
print("shape:", x.shape)

#Criação de valores dentro de um intervalo
#linspace = retorna números linearmente espaçados dentro de um range específico
print('---------- Ex valores uniformes entre 5 e 15 ----------')
x_min, x_max = 5, 15
x = np.linspace(start=x_min, stop=x_max, num=6) #bom para regressão linear
print("x:", x)
print("shape:", x.shape)


#Criação de Matriz identidade (matriz quandrada onde diagonal principal formada só por 1's, fora dela todos sao zeros)
print('---------- Matriz identidade ----------')
n = 8
x = np.eye(n)
print("x:\n", x)
print("shape:", x.shape)

#criação de valores aleatórios floats entre 0 e 1:
#np.random.seed(10)
print('---------- valores aleatórios ----------')
x = np.random.random(size=(2, 3)) #2 e 3 são as dimensoes da matriz
print("x:\n", x)
print("shape:", x.shape)


"""
- Indices ao longo de uma dimensão variam de 0 a n-1
(n é o número de elemntos da dimensão) (cada posiçõo da matriz é representada por um índice)
EX: Index = 4

A =  88  19  46  74  94

A[1]->19
A[4]->94

- Acessando elementos: Índices negativos significam que o array será acessado de trás para frente
A[-1]->94
A[-2]->74
etc.

- Acessando elementos de array

EX:
B =
88 19 46 74 94
69 79 26 07 29
21 45 12 80 72
28 53 65 26 64
71 96 34 61 52

B[2,1]->45
[linha(axis 0), coluna(axis 1)]
B[i, j]

- Slicing = fatiamento [primeiro, último - 1] (OBS: retorna um numpy array reduzido que contém os valores selecionados)
EX:
A = 88 19 46 74 94

A[1:3]-> 19 46
--------------------------------------
EX: Slicing em uma matrix:
B =
88 19 46 74 94
69 79 26 07 29
21 45 12 80 72
28 53 65 26 64
71 96 34 61 52

B[1:3, 1:4] ->
[1:até o 3, 1:até o 4] (Segundo elemento: 3-1 e 4-1)

79 26 7
45 12 80


B[i:k, j:l]
K e l não entram no slicing, e sim k - 1 e l - 1

"""
import numpy as np
print('-----------------------1----------------------------------- ')
#Os índices no Py vão de 0 a n-1, n é o tamanho da dimensão:
x = np.linspace(start=10, stop=100, num=10)
print("x:", x)
print("shape", x.shape)


print('------------------------2---------------------------------- ')
#Extração de elementos:
print("x:", x)
print("primeiro elemento", x[0])
print("segundo elemento elemento", x[1])
print("último elemento", x[9])
print("último elemento", x[-1])


print('-------------------------3--------------------------------- ')
#Slicing: extração de subarrays:
print("x:", x)
print("dois primeiros elementos", x[0:2])
print("dois primeiros elementos", x[:2])
print("dois últimos elementos", x[-2:])


print('-------------------------4--------------------------------- ')
#Slicing em arrays 2D (matrizes) (reshape = redimensionar o arquivo original)
#Pega 1D de 10 elementos e transf em 2D de tb 10 elementos:
x = x.reshape(2, 5) #reshape de x para 2 linhas e 5 colunas
print("x:\n", x)


print('-------------------------5--------------------------------- ')
#Extração de elementos:
print("primeira linha, segunda coluna", x[0, 1])
print("segunda linha, penúltima coluna", x[1, -2])
print("última linha, última coluna", x[1, 4])
print("última linha, última coluna", x[-1, -1])


print('-------------------------6--------------------------------- ')
#Slicing: extração de suarrays:
print("x:\n", x)
print("primeira linha inteira: ", x[0, :])
print("primeira linha, segunda e quarta coluna: ", x[0, 1:4])
print("última coluna inteira:\n ", x[:, [-1]]) #Passar entre [] para preservar a dimensao atual


print('-------------------------7--------------------------------- ')
#Atenção com compartilhamento de memória em subarrays:
x = np.array([1, 2, 3])
print("x antes:", x)
y = x[:2] #extração dos elementos
y[0] = -100 #alteração do valor em y altera o valor de x
print("x depois:", x)



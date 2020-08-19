"""
- Operações elemento a elemento:
Soma:
"+" ou
np.add

Subtração:
"-" ou
np.subtract

Divisão:
"/" ou
np.divide

Multiplicação:
"*" ou
np.multiply

EX: SOMA
u = [1/0]
v = [0/1]
operação com vetores u + v = [(1+0)/(0+1)] = [1/1]

EX: A multiplicação é feita elemento a elemento conforme suas posições (equivalentes)

-------------------------------------------------------------------------------------------
- Broadcasting:

y = [1/2]
2y = [2(1)/2(2)] = [2/4]

Permite fazer operaçoes entre diferentes dimenoes (2D com 1D)...

--------------------------------------------------------------------------------------------
- Operações matriciais:

Multiplicação de matrizes:

-Python puro: A @ B

-Numpy:
np.dot(A,B)
A.dot(B)

"""
import numpy as np

print('------------------------1---------------------------')
#criação de dois arrays x e y
x = np.ones((2, 2))
y = np.eye(2)
print("x: \n", x)
print("y: \n", y)

print('------------------------2---------------------------')
#Soma
print("soma de dois arrays:\n", x + y)
print("soma com float/int: \n", x + 2) #broadcasting

print('------------------------3---------------------------')
#Subtração
print("subtração de dois arrays:\n", x - y)
print("subtração com float/int: \n", x - 2) #broadcasting

print('------------------------4---------------------------')
#divisão
print("divisão de dois arrays:\n", x / y)
print("divisão com float/int: \n", x / 2) #broadcasting


print('------------------------5---------------------------')
# quando o broadcasting não funciona
#np.array([1, 2, 3)] + np.array([1, 2)]
#OBS: AS DIMENSOES PRECISAM SER CONSISTENTES!!!

print('Para o np broadcasting funcionar as dimensões precisam ser consistentes')

print('------------------------6---------------------------')
#Soma, subtração e divisão:
print("Combinação de operações: \n", (x+y)/(x-2))

#------------------------------------------------------------------------------------------------------
#Operações matriciais:

print('------------------------1---------------------------')
#Multiplicação elemento a elemento
print("multiplicação de dois arrays:\n", x * y)
print("Multiplicação com float/int: \n", x * 2) #broadcasting


print('------------------------2---------------------------')
#Multiplicação matricial
print("multiplicação matricial (np.dot):\n", np.dot(x, y))
print("multiplicação matricial (@):\n", x @ y)
print("multiplicação matricial (.dot):\n", x.dot(y))


print('------------------------Exemplo---------------------------')
"""
EXEMPLO
Solução de um sistema de equações:

a + 2*b = 7
3*a - 2*b = -11

solução analitica: (a, b) = (-1, 4)
Matricialmente, este problema tem a seguinte forma:

Ax = c, onde:
- x = [a, b]
- A = [[1, 2], [3, -2]]
- c = [7, -11]

solução numérica: x = inv(A) @ c, 
"""
#definição do problema:
A = np.array([[1, 2], [3, -2]])
c = np.array([[7], [-11]])
print("A: \n", A)
print("c: \n", c)


print('------------------------Para encontrar a solução analitica---------------------------')
#solução pela inversa da matriz A * c
x = np.dot(np.linalg.inv(A), c)
#ou x = np.linalg.inv(a) @ c
print("(a, b):", x.ravel())


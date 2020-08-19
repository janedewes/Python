"""
- Comparações
- Indexação booleana
"""
import numpy as np
#comparações booleanas
A = np.array([1, 2, 3])
B = np.array([2, 0, 2])
s = 3

#menor
print("comparação menor: ")
print(A < B)
print(A < s)

#menor ou igual
print("comparação menor ou igual:")
print(A <= B)
print(A <= s)

#maior
print("comparação maior: ")
print(A > B)
print(A > s)

#maior ou igual
print("comparação maior ou igual:")
print(A >= B)
print(A >= s)


#igual
print("comparação igualdade: ")
print(A == B)
print(A == s)

print('------------------ Indexação booleana ----------------- ')
#indexação booleana: um novo subarray contendo uma cópia dos elementos em que a condição de verificação se aplica:
cond = A <= 2
D = A[cond]
print("A:", A)
print("condição:", cond)
print("D:", D)


print('----------------------------------------------- Prática ----------------------------------------- ')

print('------------------1----------------- ')
x = np.array([[1, 2], [3, 4]])
y = np.array([1.5, 3.5])
print("x: \n", x)
print("y: \n", y)


print('------------------2----------------- ')
#comparações ponto a ponto
print("Comparação de um array com um escalar (>): \n", x > 2)
print("Comparação de um array com um escalar (>=): \n", x >= 2)
print("Comparação de um array com um escalar (<): \n", x < 2)
print("Comparação de um array com um escalar (<=): \n", x <= 2)

print("Comparação entre arrays (==): \n", x > x)
print("Comparação entre arrays (>): \n", x > x)
print("Comparação entre arrays (>): \n", x > y) #broadcasting



print('------------------3----------------- ')
#Indexação booleana:
x = np.array(([1, 3, 7],
              [4, 11, 21],
              [42, 8, 9]))
print("x: \n", x)

#indexação booleana: retornar o número de elementos maiores que k
k = 10
cond = x > k
print("condição: \n", cond)
print(f"elementos maiores que {k}: ", x[cond])
print(f"número de elementos maiores que {k}: ", len(x[cond]))


print('------------------4----------------- ')
#indexação booleana: extração de números pares
cond = x % 2 == 0 #números pares
print("condição: \n", cond)
print("números pares: ", x[cond])


print('------------------FIM----------------- ')


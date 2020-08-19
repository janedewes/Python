"""
Modelo de Classificação no Scikit-learn
"""
import pandas as pd
import numpy as np

print("-----------------------------------Aquivo CSV----------1--------------------------------------------------------")

#leitura dos dados csv
df = pd.read_csv("https://pycourse.s3.amazonaws.com/temperature.csv") #em uma máq local = colocar o caminho para o arquivo
print(df.head())

print("-----------------------------------------------------2----------------------------------------------------------")

#extração de x e y:
x, y = df[['temperatura']].values, df[['classification']].values
print("x: \n", x)
print("y: \n", y)

print("----------------------------------------------3-----------------------------------------------------------------")
#pré-processamento
from sklearn.preprocessing import LabelEncoder

#Conversão de y para valores numéricos
le = LabelEncoder() #label encoder
y = le.fit_transform(y.ravel())
print("y: \n", y)

print("---------------------------------------------4------------------------------------------------------------------")

#modelo
from sklearn.linear_model import LogisticRegression

#Classificador
clf = LogisticRegression()
clf.fit(x, y) #calcular a fç que melhor discrimina os dados (coefs da fç)

print("---------------------------------------------5------------------------------------------------------------------")

#Gerando 100 valores de temperatura (só temos 6 no dataset)
#linearmente espaçados entre 0 e 45
#predição em novos valores de temperatura
x_test = np.linspace(start=0., stop=45., num=100).reshape(-1, 1)

#predição desses valores
y_pred = clf.predict(x_test)
#resultado do modelo: (Retorna em valores númericos)
print(y_pred)
#conversão de y_pred de volta ao valores originais
y_pred = le.inverse_transform(y_pred)
print(y_pred)

print(x_test)

print("---------------------------------------------6------------------------------------------------------------------")

#colocar os dados em um pandas data frame
#output
output = {'new_temp': x_test.ravel(),
          'new_class': y_pred.ravel()}
output = pd.DataFrame(output)

#Estatisticas
output.info()

#Estatisticas
output.describe()

print("---------------------------------------------7------------------------------------------------------------------")

#contagem de valores gerados
output['new_class'].value_counts().plot.bar(figsize=(10, 5),
                                            rot=0,
                                            title="# de novos valores gerados");


print("---------------------------------------------8------------------------------------------------------------------")

#Distribuição do output produzido (mediana, percentil etc)
#conseguimos inferir a classificação novas temperaturas a partir de um dataset com 6 exemplos
output.boxplot(by='new_class', figsize=(10, 5));

print("--------------------------------------Exemplo------------------------------------------------------------------")

#Sistema automático
def classify_temp():
    """classifica o input do usuário"""

    ask = True
    while ask:
        #input de temperatura
        temp = input("insira a temperatura (graus celsius): ")

        #transformar para numpy array
        temp = np.array(float(temp)).reshape(-1, 1)

        #realiza classificação
        class_temp = clf.predict(temp)

        #transformação inversa para retornar a string original
        class_temp = le.inverse_transform(class_temp)

        #classificação
        print(f"A classificação da temperatura {temp.ravel()[0]} é: ", class_temp[0])

        #perguntar
        ask = input("Nova classificação (y/n): ") == 'y'


#rodando programa
classify_temp()
print("-------------------------------------------Fim------------------------------------------------------------------")



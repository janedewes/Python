#importar as bibliotecas
import pandas as pd

print("-----------------------------------Aquivo CSV------------------------------------------------------------------")

#leitura dos dados csv
df = pd.read_csv("https://pycourse.s3.amazonaws.com/temperature.csv") #em uma máq local = colocar o caminho para o arquivo
print(df)

#leitura de planilhas excel, 2 abas (worksheets)
#leitura do aquivotodo
excel_file = pd.ExcelFile("https://pycourse.s3.amazonaws.com/temperature.xlsx")
print("---------------------------------------Primeira aba excel------------------------------------------------------")
#Leitura da primeira aba(Sheet1)
#dados numericos com separador decimar = '.'
df2 = pd.read_excel(excel_file, sheet_name='Sheet1')
print(df2)

print("----------------------------------------Segunda aba excel------------------------------------------------------")
#Leitura da segunda aba(Sheet2)
#dados numericos com separador decimar = ','
df3 = pd.read_excel(excel_file, sheet_name='Sheet2', decimal=',')
print(df3)

print("---------------------------------------------------------------------------------------------------------------")

#Vizualizando as primeiras n linhas?
n = 3
df.head(n)


#Vizualizando as últimas n linhas
n = 3
df.tail(n)

#dtypes
df.dtypes

#estatísticas básicas
df.describe()

#dataframe info
df.info()

#nomes das colunas
df.columns

#alterar valores das colunas
df.columns = ['col1', 'col2', 'col3']

print('-------------------------------------------------fim-----------------------------------------------------------')

"""
- Indexação
Prática da aula de PandasIndexacao.py
* metodo iloc()
* metodo loc()
"""
#seleção de uma coluna
df['date']

#tipo
type(df['date'])

#seleção de múltipas colunas
df[['date', 'classification']]

#iloc
help(df.iloc)

#indexação por índice
#selecionando todas as linhas e a coluna 1
#coluna 1: temperatura
df.iloc[:, 1]

#indexando por nome
#selecionando todas as linhas e a coluna 1
df.loc[:, 'temperatura']

#indexação por índice de múltiplas colunas
df.iloc[:, 1:3] #obs: 3 é exclusivo (vai até o 2)


#indexação por nome de múltiplas colunas
df.loc[:,['temperatura', 'classification']]

#indexação por nome de múltiplas colunas
df.loc[:, 'temperatura']

print('-------------------------------------------------fim-----------------------------------------------------------')

#dtype
df.dtypes

#transformando o tipo da coluna date para datetime
df['date'] = pd.to_datatime(df['date'])
df.dtypes


#setando o índice
df = df.set_index('date')
#visualizando o índice
df

#5 primeiras linhas
df.head(5)

#INDEXAÇÃO BOOLEANA

#indexação booleana
#selção de exemplos acima de 25 graus (mesma opção do cond do numpy)
df[df['temperatura'] >= 25]

#indexação booleana considerando datetime
#seleção de entradas até Março de 2020
df[df.index <= '2020-03-01']

#indexação booleana considerando datetime
# seleção de entradas até Março de 2020 e slice na coluna classification
df.loc[df.index <= '2020-03-01', ['classification']]


#indexação booleana considerando datetime
# seleção de entradas até Março de 2020 e slice na coluna classification
df.iloc[df.index <= '2020-03-01', [-1]]


print('-------------------------------------------------fim-----------------------------------------------------------')



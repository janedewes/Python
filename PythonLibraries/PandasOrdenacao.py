"""
- Ordenação no pandas: Organizar o dataframe de acordo com uma ordem específica (crescente/decrescente.... etc)

*Método sort_values

df.sort_values(by=['col1']) (ordem crescente)

df.sort_values(by='col1', ascending=False) (decrescente)

df.sort_values(by=['col1', 'col2']) (ordenar por mais de uma coluna)

df.sort_values(by='col1', na_position='first') (Para o NaN aparecer nas primeiras posições)

"""

"""
Métodos: sort_values e sort_index

"""
#Ordenação (Análise do dataframe da aula passada)

#df.sort_values
df.sort_values?

#ordenação crescente por uma coluna
df.sort_values(by='temperatura')

#ordenação crescente por uma coluna
df.sort_values(by='classification')

#ordenação crescente por mais uma coluna
df.sort_values(by=['classification', 'temperatura'])

#ordenação descrescente por uma coluna
df.sort_values(by='temperatura', ascending=False)

#ordenação crescente pelo índice
df.sort_index()

#ordenação decrescente pelo índice
df.sort_index(ascending=False)

print(----------------------------------------------fim----------------------------------------------------------------)

#Visualização no pandas (plot de linhas, barras, setores(pizza)

#plot de linhas
df.plot()

#plot de linhas: tamanho
df.plot(figsize=(10, 5));

#plot de linhas : grid
df.plot(figsize=(10, 5), grid=True);

#plot de linhas: style
df.plot(style='-o', figsize=(10, 5), grid=True);
df.plot(style='--', figsize=(10, 5), grid=True);
df.plot(style='-.', figsize=(10, 5), grid=True);


#plot de linhas: linewidth (grossura da linha)
df.plot(style='-.', linewidth=2, figsize=(10, 5), grid=True);


#plot de linhas: color
df.plot(style='-.', linewidth=2, color='red', figsize=(10, 5), grid=True);


#plot de linhas: color
df.plot(style='-.', linewidth=2, color='#822fb5', figsize=(10, 5), grid=True);


df['classification'].value_counts()
#plot de barras
df['classification'].value_counts().plot.bar(figsize=(10, 5),
                                             rot=0);


#plot de barras (rot = rotação)
df.plot(kind='bar', figsize=(10, 5), rot=30);


#pie plot
df['classification'].value_counts().plot.pie(autopct='%1.1f%%', #coloca a % com 1 casa decimal
                                             shadow=True,
                                             figsize=(10, 7));


print(----------------------------------------------fim----------------------------------------------------------------)

"""
Dicas gerais sobre o pandas

- Método groupby
- Operações inplace
- Compartilhamento de memória em cópias

"""

#Mesmo dataframe das outras aulas
df.head(6)


#groupby : agrupamento por valores únicos de uma ou mais colunas
df.groupby(by='classification')


#groupby : agrupamento por valores únicos de uma ou mais colunas
df.groupby(by='classification').mean() #(media)


#groupby : agrupamento por valores únicos de uma ou mais colunas
df.groupby(by='classification').sum() #(soma)


#drop: remoção de uma coluna
df.drop('temperatura', axis=1)


#cópia de um dataframe: evita compartilhamento de memória
#sem copy(), operações inplace em df2 tambem alteram df
df2 = df.copy()


#argumento inplace
# inplace = True aplica a transformação no próprio objeto
df2.drop("temperatura", axis=1)

#sem inplace, df2 continua o mesmo
df2.head()

#argumento inplace
# inplace = True aplica a transformação no próprio objeto
df2.drop("temperatura", axis=1, inplace=True)

#com inplace, df2 é alterado
df2.head()

#df
df.head()


print(----------------------------------------------fim----------------------------------------------------------------)









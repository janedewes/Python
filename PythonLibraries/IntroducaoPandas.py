"""
- Introdução ao pandas

Pandas é um pacote em Py desenv para disponibilizar estruturas de dados rápidas e flexíveis para se trabalhar com dados
"relacionais" ou "rotulados". Ele pe adequado para diversos tipos de dados:

* dados tabulados com colunas de tipos heterogenios, como por ex em tabelas SQL ou planilhas excel.
* dados de séries temporais ordenados ou não ordenados.
* dados matriciais arbitrários, com linhas e colunas.

* flexível: Escrita em cima do numpy, possui metodos do matplotlib, usado em conjunto com outras bibliotecas de ciencia de dados(scipy, scikit-learn etc).
* Instalação: pip install pandas ou conda install pandas.
* importando no ambiente de desenv.: import pandas as pd.

* Pandas é uma forma de carregar dados e utilizar no Numpy. Ferramenta que lê dados.
------------------------------------------------------------------------------------------------------------------------
- Dtypes e tipos de objetos

* DataFrames(tabela) e Series.
------------------------------------------------------------------------------------------------------------------------
- Leitura de dados

* Para leitura depende do formato do dado de entrada:
read_csv
read_json
read_excel

- Aplicações
* tratamento de daod faltantes (representados por NaN)
* tamanhos mutáveis: colunas podem ser inseridas e excluidas de DataFrames com facilidade
* grupo de funcionalidades poderoso e flexivel para agregar e transformar conj de dados
* ferramentas de IO robustas para leitura de dados de arquivos como CSV, Excel e banco de dados. Entre outros.

"""
"""
Introdução ao ML

- Arthur Samuel(1959): ML is the field of study that gives the computer the ability to learn without being explicitly
programmed.
- ML usa um conj de ferramentas para modelagem e análise de dados denominado aprendizado estatístico.
- Abordagem estatística para o problema de ML : Desenvolvimento de modelos capazes de aprender a partir de dados.

- Abordagem simbólica: Suponha que exista um algoritmo capaz de contar o número de retas e curvas de uma imagem de um dígito:
Se digito é composto por uma reta então "um"
Se dígito é composto por uma ou mais curvas então "dois"
Se dígito é composto por tres retas então "quatro"
- Dificuldade de modelagem de todo o problema
- Dificuldade de lidar com incertezas, informações imprecisas etc.

- Aprendizado estatístico
Aprendizado a partir de dados.
Inferencias a partir de experiencias passadas

" Seu modelo é tão com quanto forem os dados que o alimentam..."

- Exemplos de problemas:
* Reconhecimento de dígitos escritos a mão.
* Deteção facial.
* Geração automática de legendas de fotos.

- Pipeline (ciclo percorrido pelo cientista de dados, todo processo)

- Identificar se é um problema de: REGRESSÃO, CLASSIFICAÇÃO, AGRUPAMENTO, SERIES TEMPORAIS....PARA FORECASTING(PREVISÃO) ETC

"""

"""
Introdução ao Scikit-learn

- O Scikit-learn é um dos mais usados frameworks de ML em PY para:
* Classificação 
* Regressão
* Redução de dimensionalidade
* Seleção de modelos
* Clustering (agrupamento)
* Pré-processamento 

- Open-source
- Desenvolvido baseado no numpy, scipy e matplotlib.
- Interface alto-nível de modelos complexos. 
- Instalação: 
pip install scikit-learn
conda install scikit-learn

- Uso: Usar em partes, pois ela é muito grande
#pré-processamento 
from sklearn.preprocessing import LabelEncoder

#modelo
from sklearn.linear_model import LogisticRegression

- Possui diversos datasets disponíveis 
Dataset examples: sklearn.datasets 
------------------------------------------------------------------------------------------------------------------------

- Exemplo de execução de um problema complexo em poucas linhas:

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

xx, yy = np.meshgrid(np.linspace(-3, 3 500), 
                    np.linspace(-3, 3, 500))
                    
np.random.seed(0)
X = np.random.randn(300, 2)
Y = np.logical_xor(X[:,0] > X[:,1] > 0)

#fit the model
clf = smv.NuSVC(gamma='auto')
clf.fit(X, Y)

------------------------------------------------------------------------------------------------------------------------
"""

"""
- Classificação de padrões conceitos básicos

Classificação: Valores discretos (saídas são classes)
g(X): fronteira de decisão - reta que melhor separa duas classes (por ex)

*Um classificador binário:
1, caso g(X) : limiar
0, caso contrário

*Fronteira de decisão

Regressão: Valores contínuos (-infinito para +infinito)
"""
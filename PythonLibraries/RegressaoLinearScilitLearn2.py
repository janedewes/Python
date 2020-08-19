"""
Métrica R2 (coef de determinação de um modelo de regressao)

* Quão bom meu modelo é em relação ao modelo que prevê sempre a média
* e o modelo que prevê sempre a média é o modelo baseline

* Erro quadratico medio =  é uma medida do quão bom/distante o meu modelo está dos valores reais dos meus dados.
(è a diferença o valor que o modelo diz q o dado tem em relação ao valor que ele realmente tem, ou seja, distancia
do dado à reta de regressão)
Media = pq é a soma de todas as diferenças (de todos os valores)

OBS: MSE (ver as 3 formulas)
R2 é comparado com o modelo baseline

"""
#continuação da aula 1:
#fç para cálculo de MSE
def mse(y_true, y_pred, is_ref =  False):

    #mse modelo
    if is_ref:
        mse = ((y_true - y_true.mean())**2).mean()
    else:
        mse = ((y_true - y_pred))**2.mean()

    return mse

#fç para cálculo do coef de determinação R2
def r2(mse_reg, mse_ref):
    return 1 - mse_reg/mse_ref

#vizualização y e y_pred
print("y_true:", y.ravel())
print("y_pred:", y_pred.ravel())

#calculando o mse dos modelos
mse_reg = mse(y_true=y, y_pred=y_pred)
print("MSE do modelo de regressão: ", mse_reg)
mse_ref = mse(y_true=y, y_pred=y_pred, is_ref=True)
print("MSE do modelo de referencia: ", mse_ref)

#calculando o R2 do score
r2_score = r2(mse_reg=mse_reg, mse_ref=mse_ref)
print("Coenficiente R2 do modelo implementado (calculado):", r2_score)

#score retornado pelo scikit-learn
r2_score_skl = reg.score(x, y)
print("Coeficiente R2 do modelo implementado (scikit-learn: ", r2_score_skl)

#fim!!!





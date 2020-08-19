"""
- Indexação no pandas:
* Método iloc()
* Método loc()

- Indexação booleana
"""

"""
- Indexação direta
 
 data_frame["temperatura"]
 data_frame[['temperatura', 'classification']]
------------------------------------------------------------
 * Método iloc()
 
 Similar à indexação no numpy (indexando pelo valor)
 data_frame.ilod[i_linha, j_coluna]
 
 Sclicing: 
 data_frame.iloc[i:k, j:l]
 
------------------------------------------------------------
 * Método loc() (usa o nome da linha ou coluna, facilita o acesso)
 
 data_frame.loc[nome_linha, nome_coluna]
 
 ------------------------------------------------------------
 
 - Indexação booleana
 
 df[df['classification']=='quente']
 
  df.loc[df['classification']=='quente', 'temperatura']
 
"""
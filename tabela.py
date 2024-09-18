import numpy as np
cod = np.array([[4, 1], [3, 1]])

decod = np.linalg.inv(cod)

#Tabela de A - Z
tabela = {}
for i, letra in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ", start=1):
    tabela[letra] = i

tabela[" "] = 27
tabela ["!"]= 28
tabela [""] = 0
tabela["Ç"] = 29
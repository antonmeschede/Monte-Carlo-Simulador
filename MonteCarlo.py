import pandas as pd
import numpy as np
import pandas_datareader.data as wb
import datetime as dt
import matplotlib.pyplot as plt


print('Simulador Monte Carlo')
print()
print('Este é um script simples que utiliza dados do yahoo finance para entregar uma simulação monte carlo de uma ação indicada pelo usuário.')
print()
print('As simulações de Monte Carlo são usadas para modelar a probabilidade de resultados diferentes em um processo que não pode ser facilmente previsto devido à intervenção de variáveis aleatórias.')
print()

nome = str(input('Olá, Qual o seu nome? '))
print(f'Prazer, {nome}! Hoje iremos rodar algumas simulações.')

ativo = str(input('Qual ação você deseja analisar? '))
resposta = str(ativo + '.SA')
começo = str(input('Qual a data inicial? [AAAA-MM-DD] '))
fim = str(input('Qual a data final? [AAAA-MM-DD] '))

preços = wb.DataReader(resposta, data_source='yahoo', start=começo, end=fim)['Close']
retorno = preços.pct_change()

último_preço = preços[-1]

qde_simulações = int(input('Quantas simulações deseja rodar? '))
qde_dias = 252

df_simulação = pd.DataFrame()

for x in range(qde_simulações):
    count = 0
    vol_diaria = retorno.std()

    lista_preço = []

    preço = último_preço * (1 + np.random.normal(0, vol_diaria))
    lista_preço.append(preço)

    for y in range(qde_dias):
        if count == 251:
            break
        preço = lista_preço[count] * (1 + np.random.normal(0, vol_diaria))
        lista_preço.append(preço)
        count += 1

    df_simulação[x] = lista_preço

fig = plt.figure()
fig.suptitle(f'Monte Carlo {ativo}')
plt.plot(df_simulação)
plt.axhline(y= último_preço, color = 'r', linestyle = '-')
plt.xlabel('Dia')
plt.ylabel('Preço')
plt.show()

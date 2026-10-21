import numpy as np

# Dados de exemplo
print('\n')
dados = np.array([12, 15, 17, 20, 22, 25, 28, 30, 35, 40, 80])
print(dados)

# Calculando os quartis
q1 = np.percentile(dados, 25)
q2 = np.percentile(dados, 50)
q3 = np.percentile(dados, 75)

print(f'Primeiro Quartil: {q1}')
print(f'Mediana: {q2}')
print(f'Terceiro Quartil: {q3}')

i = q3 - q1
Limite_inferior = q1 - 1.5 * i
Limite_superior = q3 + 1.5 * 1
outliers = dados[(dados < Limite_inferior) | (dados > Limite_superior)]
dentro = dados[(dados >= Limite_inferior) & (dados <= Limite_superior)]
bigode_inferior = dentro.min()
bigode_superior = dentro.max()

print(f'Limite inferior: {Limite_inferior}')
print(f'Limite superior: {Limite_superior}')
print(f'outliers: {outliers}')
print(f'dentro: {dentro}')
print(f'bigode inferior: {bigode_inferior}')
print(f'bigode superior: {bigode_superior}')
print('\n')
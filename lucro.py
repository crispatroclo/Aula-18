import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\cristiane.patroclo\Downloads\funcionarios.csv")
#print(df)

lucro = df['lucro'].to_numpy()
print('lucro')
print(lucro)
print('\n')

print('lucro ordenado')
print(np.sort(lucro))
print('\n')

q1 = np.percentile(lucro, 25)
q2 = np.percentile(lucro, 50)
q3 = np.percentile(lucro, 75)

print(f'Primeiro Quartil: {q1}')
print('\n')

print(f'Mediana: {q2}')
print('\n')

print(f'Terceiro Quartil: {q3}')
print('\n')

i = q3 - q1
Limite_inferior = q1 - 1.5 * i
Limite_superior = q3 + 1.5 * 1
outliers = lucro[(lucro < Limite_inferior) | (lucro > Limite_superior)]
dentro = lucro[(lucro >= Limite_inferior) & (lucro <= Limite_superior)]
bigode_inferior = dentro.min()
bigode_superior = dentro.max()

print(f'i: {i}')
print('\n')

print(f'Limite inferior: {Limite_inferior}')
print('\n')

print(f'Limite superior: {Limite_superior}')
print('\n')

print(f'outliers: {outliers}')
print('\n')

print(f'dentro: {dentro}')
print('\n')

print(f'bigode inferior: {bigode_inferior}')
print('\n')

print(f'bigode superior: {bigode_superior}')
print('\n')

print('\n')
print('\n')

plt.boxplot(lucro)
plt.show()

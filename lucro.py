import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\cristiane.patroclo\Downloads\funcionarios.csv")
print(df)

lucro = df['lucro'].to_numpy()
print(lucro)

q1 = np.percentile(lucro, 25)
q2 = np.percentile(lucro, 50)
q3 = np.percentile(lucro, 75)

print(f'Primeiro Quartil: {q1}')
print(f'Mediana: {q2}')
print(f'Terceiro Quartil: {q3}')

i = q3 - q1
Limite_inferior = q1 - 1.5 * i
Limite_superior = q3 + 1.5 * 1
outliers = lucro[(lucro < Limite_inferior) | (lucro > Limite_superior)]
dentro = lucro[(lucro >= Limite_inferior) & (lucro <= Limite_superior)]
bigode_inferior = dentro.min()
bigode_superior = dentro.max()

print(f'i: {i}')
print(f'Limite inferior: {Limite_inferior}')
print(f'Limite superior: {Limite_superior}')
print(f'outliers: {outliers}')
print(f'dentro: {dentro}')
print(f'bigode inferior: {bigode_inferior}')
print(f'bigode superior: {bigode_superior}')
print('\n')

plt.boxplot(lucro)
plt.show()

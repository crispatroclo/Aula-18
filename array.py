import numpy as np

dados_vendas = np.array([12, 15, 20, 22, 25, 28, 30, 35, 150])

print(dados_vendas)
print('\n')

# media (sensivel a extremos)
media_vendas = np.mean(dados_vendas)
print(f'{media_vendas:2.1f}')
print('\n')

# mediana (robusta aextremos)
mediana_vendas = np.median(dados_vendas)
print(f'{mediana_vendas:2.1f}')
print('\n')

# q1
q1 = np.percentile(dados_vendas, 25)
print(f'{q1:2.1f}')
print('\n')

# q2
q2 = np.percentile(dados_vendas, 50)
print(f'{q2:2.1f}')
print('\n')

# q3
q3 = np.percentile(dados_vendas, 75)
print(f'{q3:2.1f}')
print('\n')
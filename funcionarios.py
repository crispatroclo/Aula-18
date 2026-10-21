import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\cristiane.patroclo\Downloads\funcionarios.csv")
print(df)

salario = df['salario'].to_numpy()
print(salario)

# media (sensivel a extremos)
media = np.mean(salario)
print(f'{media:4.1f}')

# mediana (robusta aextremos)
mediana =np.median(salario)
print(f'{mediana:4.1f}')

# q1
q1 = np.percentile(salario, 25)
print(f'{q1:4.1f}')

# q2
q2 = np.percentile(salario, 50)
print(f'{q2:4.1f}')

# q3
q3 = np.percentile(salario, 75)
print(f'{q3:4.1f}')
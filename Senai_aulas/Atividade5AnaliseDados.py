# Importar CSV e analisar

import pandas as pd

taxis = pd.read_csv('taxis.csv', sep=',')
print(taxis)

print('3333333333333333')
print(taxis.groupby('local')['tip'].max())
print('3333333333333333')
print(taxis['local'].value_counts())
print(taxis.groupby(['local'])['tip'].agg(['mean','median']))

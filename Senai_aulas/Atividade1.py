##### Usuário digitar 10 numeros e colocar array, calcular, média, minimo, máximo, desvio padrão,
import numpy as np
array_zeros=np.zeros(10)
print(array_zeros)
i = 0
for i in range(10):
    numero = str(input('Digite 1 numero para incluir no array: '))
    print(numero)
    array_zeros[i]= numero
    if i ==10 :
        break
print(array_zeros)
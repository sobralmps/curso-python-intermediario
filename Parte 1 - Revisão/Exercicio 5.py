# -*- coding: utf-8 -*-

#        EXERCÍCIO 5

from time import sleep

print("\nPrograma que cria uma lista de 1 até 10 e printa os números de 1 por 1 através da estrutura while.\n")

sleep(1)

x = 0
y = 0
numeros = []

while x < 10:
    x += 1
    numeros.append(x)

sleep(0.5)

while y < (len(numeros)):
    y += 1
    print(numeros[y-1])

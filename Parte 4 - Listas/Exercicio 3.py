# -*- coding: utf-8 -*-

#        EXERCÍCIO 3

from time import sleep

print("\nPrograma que divide os números pares e ímpares inseridos em duas diferentes listas.\n")

pares = []
impares = []

sleep(1)

for i in range(6):
    num = int(input(f"Digite o {i+1}º número: "))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f"\nLista com os números pares: {pares}\nLista com os números ímpares: {impares}")

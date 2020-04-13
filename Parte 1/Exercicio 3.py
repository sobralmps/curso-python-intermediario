#-*- coding: utf-8 -*-

#        EXERCÍCIO 2

from time import sleep

print("\nPrograma que cria uma lista de 1 até 10 e multiplica os números por três\n")

sleep(1)

lista = []

for i in range(1, 10+1):
    lista.append(i)

print(f"Lista antes da multiplicação: {lista}\n")

sleep(0.5)

for i in range(len(lista)):
    lista[i] = (i+1) * 3

print(f"Lista após a multiplicação: {lista}")

#-*- coding: utf-8 -*-

#        EXERCÍCIO 1

from time import sleep

print("\nPrograma que verifica se o número inserido é positivo ou negativo. Utilizando [def].\n")

sleep(1)


def verifica(num):
    if num < 0:
        saida = "Número negativo."
    elif num > 0:
        saida = "Número positivo."
    else:
        saida = "Número neutro."
    return saida


sleep(0.5)

numero = int(input("Insira o número: "))

print(verifica(numero))

#-*- coding: utf-8 -*-

#        EXERCÍCIO 3

from time import sleep

print("\nPrograma que verificar se o número é par ou ímpar.\n")

sleep(1)


def verifica(numero):
    if numero % 2 == 0:
        saida = "\nO número é par"
    else:
        saida = "\nO número é ímpar"
    return saida


sleep(0.5)

num = int(input("Insira o número para verificação: "))

print(verifica(num))

# -*- coding: utf-8 -*-

#        EXERCÍCIO 2

from time import sleep

print("\nPrograma que soma os elementos de um tupla que contenha N números.\n")

sleep(1)


def soma(*valores):
    soma = 0
    for numero in valores:
        soma += numero
    return print(f"A soma dos valores {valores} é igual a {soma}.")


soma(1, 5, 3)

# -*- coding: utf-8 -*-

#        EXERCÍCIO 4

from time import sleep

print("\nPrograma que mostra o maior número entre os elementos de um tupla que contenha N números.\n")

sleep(1)


def maior(*valores):
    maior = 0
    for numero in valores:
        if numero > maior:
            maior = numero
    return print(f"O maior número dos valores {valores} é o número {maior}.")


maior(1, 5, 3, 6, 4, 3, 8)

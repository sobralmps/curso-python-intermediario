#-*- coding: utf-8 -*-

#        EXERCÍCIO 2

from time import sleep

print("\nPrograma que calcula a área de um retângulo.\n")

sleep(1)


def calculaArea(a, b):
    area = a*b
    return area


sleep(0.5)

base = int(input("Insira o comprimento da base do retângulo: "))
altura = int(input("\nInsira a altura do retângulo: "))

print(f"\nA área do retângulo é {calculaArea(base, altura)}")

# -*- coding: utf-8 -*-

#        EXERCÍCIO 4

from time import sleep

print("\nPrograma que retorna a tabuada de operações básicas de um número inserido pelo usuário.\n")

sleep(1)


def tabuada(numero):
    print("\nTabuada de soma: ")
    for somador in range(1, 10+1):
        print(f"{numero} + {somador} = {numero+somador}")

    print("\nTabuada de subtração: ")
    for subtraidor in range(1, 10+1):
        print(f"{numero} - {subtraidor} = {numero-subtraidor}")

    print("\nTabuada de multiplicação: ")
    for multiplicador in range(1, 10+1):
        print(f"{numero} * {multiplicador} = {numero*multiplicador}")

    print("\nTabuada de divisão: ")
    for divisor in range(1, 10+1):
        print(f"{numero} / {divisor} = {numero/divisor:.2f}")


sleep(0.5)

num = int(input("Insira o número para gerar a tabuada: "))

tabuada(num)

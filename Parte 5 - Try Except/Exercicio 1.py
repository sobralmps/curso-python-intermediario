# -*- coding: utf-8 -*-

#        EXERCÍCIO 1

from time import sleep

def lerInteiro():
    while True:
        try:
            n = int(input("\nDigite um número inteiro: "))
        except ValueError:
            print("\n\33[31mERRO: digite um número inteiro válido.\33[m")
            continue
        else:
            return n

sleep(1)

n1 = lerInteiro()
print(f"\nO valor inteiro informado foi {n1}")


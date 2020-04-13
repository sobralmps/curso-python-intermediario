#-*- coding: utf-8 -*-

#        EXERCÍCIO 2

from time import sleep

print("\nPrograma que cria um loop (com while) de 0 a 100, sem numeros pares, que utilize o break no numero 51\n")

sleep(1)

i = 0

while i != 100:
    i = i + 1
    if (i % 2) != 0:
        print(i)
        if i == 51:
            break
        continue

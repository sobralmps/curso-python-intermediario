# -*- coding: utf-8 -*-

#        EXERCÍCIO 1

from time import sleep

print("\nPrograma que soletra as três palavras contidas em um vetor.\n")

sleep(1)

vetor = ["um", "dois", "tres"]

sleep(0.5)

for palavras in range(len(vetor)):
    print(f"{palavras+1}ª palavra: ")

    for letras in range(len(vetor[palavras])):
        soletre = vetor[palavras]
        print(soletre[letras])

    print("\n")

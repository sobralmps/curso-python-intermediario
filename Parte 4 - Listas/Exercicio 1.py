# -*- coding: utf-8 -*-

#        EXERCÍCIO 1

from time import sleep

print("\nPrograma que crie um loop para adicionar 5 nomes em uma lista.\n")

sleep(1)

lista = []

for i in range(5):
    nome = input("Digite um nome: ")
    lista.append(nome)

print(f"\nLista com os nomes {lista}.")

# -*- coding: utf-8 -*-

'''
Faça um programa que o usuário armazene números inteiros, e caso o número for repetido, retorne uma mensagem para
inserir outro valor. Utilize lista para essa aplicação.
'''

lista = []

quantidade = int(input("Quantos números quer armazenar? "))

for i in range(quantidade):
    num = int(input("\nDigite um número: "))
    while num in lista:
        num = int(input("\nValor já armazenado, insira outra valor: "))
    lista.append(num)

print(f"\nSua lista com os números armazenados: {lista}")


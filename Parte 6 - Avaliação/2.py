# -*- coding: utf-8 -*-

'''
Faça uma função que informe a quantidade de dígitos de um número inteiro inserido pelo usuário.
'''


def quant_dig(numero):
    string_num = str(numero)
    digitos = len(string_num)
    return print(f"\nO número {numero} tem {digitos} dígitos.")


num = int(input("Digite um número inteiro: "))

quant_dig(num)

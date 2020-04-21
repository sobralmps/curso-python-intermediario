# -*- coding: utf-8 -*-

'''
Faça uma função que receba dois valores inseridos pelo usuário. E retorna qual o número é maior ou se são iguais.
'''


def compara(numero1, numero2):
    if numero1 > numero2:
        resultado = f"\nO número {numero1} é maior que o número {numero2}."
    elif numero2 > numero1:
        resultado = f"\nO número {numero2} é maior que o número {numero1}."
    else:
        resultado = f"\nOs números são iguais."
    return print(resultado)


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

compara(num1, num2)
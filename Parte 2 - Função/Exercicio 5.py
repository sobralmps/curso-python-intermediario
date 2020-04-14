#-*- coding: utf-8 -*-

#        EXERCÍCIO 5

from time import sleep

print("\nPrograma que é uma calculadora básica.")

sleep(1)


def somar(numero1, numero2):
    return numero1+numero2


def subtrair(numero1, numero2):
    return numero1-numero2


def multiplicar(numero1, numero2):
    return numero1*numero2


def dividir(numero1, numero2):
    return numero1/numero2


verificador = 1

while verificador == 1:
    operacao = int(input("\nInsira [0] para sair, [1] para somar, [2] para subtrair,"
                         "[3] para multiplicar e [4] para dividir: "))

    if operacao == 0:
        sleep(0.5)
        print("\nEncerrando programa.")
        sleep(0.5)
        break

    numA = int(input("\nInsira o primeiro número: "))
    numB = int(input("Insira o segundo número: "))

    sleep(0.5)

    if operacao == 1:
        print(f"\nO resultado da soma é: {somar(numA,numB)}")

    elif operacao == 2:
        print(f"\nO resultado da subtração é: {subtrair(numA,numB)}")

    elif operacao == 3:
        print(f"\nO resultado da multiplicação é: {multiplicar(numA,numB)}")

    elif operacao == 4:
        print(f"\nO resultado da divisão é: {dividir(numA,numB):.2f}")

    else:
        print("\nOpção inválida. Tente novamente")

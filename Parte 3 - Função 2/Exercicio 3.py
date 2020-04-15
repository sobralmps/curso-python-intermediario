# -*- coding: utf-8 -*-

#        EXERCÍCIO 3

from time import sleep

print("\nPrograma com função escreva(), que mostra a mensagem com um tamanho adaptável.\n")

sleep(1)


def escreva(texto):
    adapt = ("-" * (len(texto) + 4))
    adapt_t = ("  " + texto + "  ")
    return print(adapt), print(adapt_t), print(adapt)


escreva("Hello World!")

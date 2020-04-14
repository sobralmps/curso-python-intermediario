#-*- coding: utf-8 -*-

#        EXERCÍCIO 2

from time import sleep

print("\nPrograma que cria uma variável string com caracteres aleatórios e gera um break quando aparecer o [$]\n")

sleep(1)

random = "23n4ui2n4ui2$n4i2ni"

sleep(0.5)

for i in range(len(random)):
    print(random[i])
    if random[i] == "$":
        break

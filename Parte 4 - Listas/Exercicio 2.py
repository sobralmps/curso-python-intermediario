# -*- coding: utf-8 -*-

#        EXERCÍCIO 2

from time import sleep

print("\nPrograma que remova plutão de uma lista de planetas.\n")

planetas = ["mercurio", "venus", "terra", "marte", "jupiter", "saturno", "urano", "netuno", "plutao"]

sleep(1)

print(f"Planetas: {planetas}")

planetas.remove("plutao")

print(f"\nLista atualizada: {planetas}.")

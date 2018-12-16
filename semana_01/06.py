# -*- coding: utf-8 -*-

# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

Raio = float(input("Entre com o valor do Raio de um círculo "))
Area = math.pi * pow(Raio,2)
print("A área de um círculo com Raio igual a {0} é de {1:.5f} unidades".format(Raio,Area))

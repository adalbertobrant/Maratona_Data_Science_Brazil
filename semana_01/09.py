# -*- coding: utf-8 -*-

# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
#
#     C = (5 * (F-32) / 9).

print("Conversor de Temperatura de Graus Farenheit para Graus Celsius")
F = float(input("Entre com a temperatura em graus Farenheit: "))
print("A temperatura em Graus Celsius é de {0:.2f}".format((5*(F-32)/9)))
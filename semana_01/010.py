# -*- coding:utf-8 -*-

#  Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
#
#  C = (5 * (F-32) / 9).

C = float(input("Entre o valor da Temperatura em Graus Celsius: "))
print("O Valor da Temperatura em Graus Farenheit é {0:.1f}ª".format((9*C + 5*32)/5))
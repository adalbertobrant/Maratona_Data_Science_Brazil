# -*- coding: utf-8 -*-

import math

#Faça um programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que
# a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area_pintada = float(input("Qual o tamanho em metros da área a ser pintada: "))
cobertura = 18.0*3.0
preco_lata = 80.00

print()
print("ATENÇÃO - 1 litro de nossa tinta cobre 3 metros quadrados de parede lisa\n")
print("Aperte Y para concordar e continuar o programa de cálculo de tinta e N para sair\n")
print()

continuar = input()

if continuar =="y" or continuar == "Y":
    print("Continuando o cálculo ...\n")
else:
    print("Saindo")
    exit(1)


if area_pintada <= cobertura:
    print("Será necessário 1 lata de tinta\nValor de R$ 80,00\n")
elif area_pintada > cobertura:
    quantidade_latas = area_pintada/cobertura
    preco_total = quantidade_latas * preco_lata
    print("Quantidade de latas de tinta para a pintura de",area_pintada,"m² será de {0:.2f}".format(quantidade_latas),"litros")
    print("Valor total gasto é de R$ {0:.2f}".format(preco_total))

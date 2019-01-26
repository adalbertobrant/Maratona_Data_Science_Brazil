# -*- coding: utf-8 -*-
import math

# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
# latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#   comprar apenas latas de 18 litros;
#   comprar apenas galões de 3,6 litros;
#   misturar latas e galões, de forma que o preço seja o menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

tamanho_metros = float(input("Entre o tamanho em metros quadrados a ser pintado = "))
# cobertura de tinta 1 litro da pra 6 metros quadrados.
# preco_lata de 18 litros = R$ 80.00
# preco_galao de tinta = R$ 25.00
# lata com 10% de folga = 17.2 litros
# galao com 10% de folga = 3.24

cobertura = tamanho_metros /6
latas = cobertura / 17.2
galoes = cobertura / 3.24

custo_latas = latas*80
custo_galoes = galoes*25

x = int(cobertura/17.2)
y = math.ceil((cobertura%17.2)/3.24)
z = x*80 + y*25

print(" ")
print("Comprando apenas latas de 18 litros você vai gastar R$ {0:.2f} Reais e {1:.2f} latas".format(math.ceil(latas)*80,math.ceil(latas)))
print(" ")
print("Comprando apenas galões de 3.6 litros você vai gastar R$ {0:.2f} Reais e {1:.2f} galões".format(math.ceil(galoes)*25,math.ceil(galoes)))
print(" ")
print("Comprando latas e galões misturado você irá gastar {0} latas, {1} galões e com o custo de R$ {2} Reais".format(x,y,z))

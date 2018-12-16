# -*- coding: utf-8 -*-

# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#
#     o produto do dobro do primeiro com metade do segundo .
#     a soma do triplo do primeiro com o terceiro.
#     o terceiro elevado ao cubo.

N_1,N_2,N_Real = input("Entre 2 números inteiros e um número real na seguinte ordem Número inteiro Número inteiro Número Real: ").split(" ")

N_1 = int(N_1)
N_2 = int(N_2)
N_Real = float(N_Real)

Produto_do_dobro_do_primeiro_com_metade_do_segundo = (2*N_1) * (N_2/2)

Soma_triplo_primeiro_com_terceiro = (3*N_1) + N_Real

Cubo_terceiro = N_Real * N_Real * N_Real

print("Produto_do_dobro_do_primeiro_com_metade_do_segundo = (2*{0}) * ({1}/2) = {2}\n".format(N_1,N_2,Produto_do_dobro_do_primeiro_com_metade_do_segundo))

print("Soma_triplo_primeiro_com_terceiro = (3*{0}) + {1} = {2:.1f}\n".format(N_1,N_Real,Soma_triplo_primeiro_com_terceiro))

print("Cubo_terceiro = {0} * {1} * {2} = {3:.1f}".format(N_Real,N_Real,N_Real,Cubo_terceiro))
